import logging
import time
from collections import OrderedDict
from .proto.attr_value_pb2 import AttrValue
from .proto.graph_pb2 import GraphDef
from .proto.node_def_pb2 import NodeDef
from .proto.step_stats_pb2 import RunMetadata, StepStats, DeviceStepStats, NodeExecStats, AllocatorMemoryUsed
from .proto.tensor_shape_pb2 import TensorShapeProto
from .proto.versions_pb2 import VersionDef
from .proto_graph import node_proto

methods_OP = ['attributeNames', 'hasMultipleOutputs', 'hasUses', 'inputs',
              'kind', 'outputs', 'outputsSize', 'scopeName']
methods_IO = [] 
backward_compat_mode = False

class NodeBase(object):
    def __init__(self,
                 debugName=None,
                 inputs=None,
                 scope=None,
                 tensor_size=None,
                 op_type='UnSpecified',
                 attributes=''):
        self.debugName = debugName
        self.inputs = inputs
        self.tensor_size = tensor_size
        self.kind = op_type
        self.attributes = attributes
        if scope is not None:
            self.scope = scope

    def __repr__(self):
        repr = []
        repr.append(str(type(self)))
        for m in dir(self):
            if '__' not in m:
                repr.append(m + ': ' + str(getattr(self, m)) + str(type(getattr(self, m))))
        return '\n'.join(repr) + '\n\n'


class NodePy(NodeBase):
    def __init__(self, node_cpp, valid_methods):
        super(NodePy, self).__init__(node_cpp)
        valid_methods = valid_methods[:]
        self.inputs = []
        global backward_compat_mode
        for m in valid_methods:
            if m == 'inputs' or m == 'outputs':
                list_of_node = list(getattr(node_cpp, m)())
                io_unique_names = []
                io_tensor_sizes = []
                for n in list_of_node:
                    if backward_compat_mode:
                        io_unique_names.append(n.uniqueName())
                    else:
                        io_unique_names.append(n.debugName())

                    if n.type().kind() == 'CompleteTensorType':
                        io_tensor_sizes.append(n.type().sizes())
                    else:
                        io_tensor_sizes.append(None)

                setattr(self, m, io_unique_names)
                setattr(self, m + 'tensor_size', io_tensor_sizes)

            else:
                if m == 'debugName' and backward_compat_mode:
                    setattr(self, m, getattr(node_cpp, 'uniqueName')())
                else:
                    setattr(self, m, getattr(node_cpp, m)())


class NodePyIO(NodePy):
    def __init__(self, node_cpp, input_or_output=None, debugName=''):
        super(NodePyIO, self).__init__(node_cpp, methods_IO)
        self.tensor_size = [] # tensor_size
        # Kind attribute string is purely descriptive and will be shown
        # in detailed information for the node in TensorBoard's graph plugin.
        #
        # NodePyOP nodes get this from their kind() method.
        self.debugName = debugName
        self.kind = 'Parameter'
        if input_or_output:
            self.input_or_output = input_or_output
            self.kind = 'IO Node'


class NodePyOP(NodePy):
    def __init__(self, node_cpp):
        super(NodePyOP, self).__init__(node_cpp, methods_OP)
        # Replace single quote which causes strange behavior in TensorBoard
        # TODO: See if we can remove this in the future
        self.attributes = str({k: node_cpp[k] for k in node_cpp.attributeNames()}).replace("'", ' ')
        self.kind = node_cpp.kind()


class GraphPy(object):
    """Helper class to convert torch.nn.Module to GraphDef proto and visualization
    with TensorBoard.

    GraphDef generation operates in two passes:

    In the first pass, all nodes are read and saved to two lists.
    One list is for input/output nodes (nodes_io), which only have inbound
    or outbound connections, but not both. Another list is for internal
    operator nodes (nodes_op). The first pass also saves all scope name
    appeared in the nodes in scope_name_appeared list for later processing.

    In the second pass, scope names are fully applied to all nodes.
    debugNameToScopedName is a mapping from a node's ID to its fully qualified
    scope name. e.g. Net1/Linear[0]/1. Unfortunately torch.jit doesn't have
    totally correct scope output, so this is nontrivial. The function
    populate_namespace_from_OP_to_IO and find_common_root are used to
    assign scope name to a node based on the connection between nodes
    in a heuristic kind of way. Bookkeeping is done with shallowest_scope_name
    and scope_name_appeared.
    """
    def __init__(self):
        self.nodes_op = []
        self.nodes_io = OrderedDict()
        self.unique_name_to_scoped_name = {}
        self.shallowest_scope_name = 'default'
        self.scope_name_appeared = []

    def append(self, x):
        if isinstance(x, NodePyIO):
            self.nodes_io[x.debugName] = x
        if isinstance(x, NodePyOP):
            self.nodes_op.append(x)
            for node_output, outputSize in zip(x.outputs, x.outputstensor_size):
                self.scope_name_appeared.append(x.scopeName)
                self.nodes_io[node_output] = NodeBase(node_output,
                                                      x.inputs,
                                                      x.scopeName,
                                                      outputSize,
                                                      op_type=x.kind,
                                                      attributes=x.attributes)

    def printall(self):
        print('all nodes')
        for node in self.nodes_op:
            print(node)
        for key in self.nodes_io:
            print(self.nodes_io[key])

    def find_common_root(self):
        for fullscope in self.scope_name_appeared:
            if fullscope:
                self.shallowest_scope_name = fullscope.split('/')[0]

    def populate_namespace_from_OP_to_IO(self):
        for node in self.nodes_op:
            for input_node_id in node.inputs:
                self.unique_name_to_scoped_name[input_node_id] = node.scopeName + '/' + input_node_id

        for key, node in self.nodes_io.items():
            if type(node) == NodeBase:
                self.unique_name_to_scoped_name[key] = node.scope + '/' + node.debugName
            if hasattr(node, 'input_or_output'):
                self.unique_name_to_scoped_name[key] = node.input_or_output + '/' + node.debugName
            if hasattr(node, 'scope'):
                if node.scope == '' and self.shallowest_scope_name:
                    self.unique_name_to_scoped_name[node.debugName] = \
                        self.shallowest_scope_name + '/' + node.debugName

        # replace name
        for key, node in self.nodes_io.items():
            self.nodes_io[key].inputs = \
                [self.unique_name_to_scoped_name[node_input_id] for node_input_id in node.inputs]
            if node.debugName in self.unique_name_to_scoped_name:
                self.nodes_io[key].debugName = self.unique_name_to_scoped_name[node.debugName]

    def to_proto(self):
        """
        Converts graph representation of GraphPy object to TensorBoard
        required format.
        """
        # TODO: compute correct memory usage and CPU time once
        # PyTorch supports it
        import numpy as np
        nodes = []
        node_stats = []
        for v in self.nodes_io.values():
            nodes.append(node_proto(v.debugName,
                                    input=v.inputs,
                                    outputsize=v.tensor_size,
                                    op=v.kind,
                                    attributes=v.attributes))

            if v.tensor_size and len(v.tensor_size) > 0:  # assume data is float32, only parameter is counted
                node_stats.append(
                    NodeExecStats(node_name=v.debugName,
                                  all_start_micros=int(time.time() * 1e7),
                                  all_end_rel_micros=42,
                                  memory=[AllocatorMemoryUsed(allocator_name="cpu",
                                                              total_bytes=int(np.prod(v.tensor_size)) * 4)]))

        return nodes, node_stats


# one argument: 'hasAttribute', 'hasAttributes',
def parse(graph, args=None, omit_useless_nodes=True):
    """This method parses an optimized PyTorch model graph and produces
    a list of nodes and node stats for eventual conversion to TensorBoard
    protobuf format.

    Args:
      graph (PyTorch module): The model to be parsed.
      args (tuple): input tensor[s] for the model.
      omit_useless_nodes (boolean): Whether to remove nodes from the graph.
    """
    import torch
    n_inputs = len(args)  # not sure...

    inputnodes = list(graph.inputs())
    global backward_compat_mode
    if not backward_compat_mode:
        try:
            inputnodes[0].debugName()
        except:
            backward_compat_mode = True

    nodes_py = GraphPy()

    for node in graph.inputs():
        if node.debugName() == 'self':
            continue
        nodes_py.append(NodePyIO(node, input_or_output='Input', debugName=node.debugName()))


    for node in graph.nodes():
        # These nodes refers to parameters such as kernel size, stride, etc.
        # The graph will be very tedious if we include all of them. So skip.
        # p.s. Those Constant will be composed by 'prim::listConstruct' and then
        # send to common OPs such as Maxpool, Conv, Linear.
        # We can let user pass verbosity value to dicide how detailed the graph is.
        if node.kind()=='prim::Constant':
            continue

        # By observation, prim::GetAttr are parameter related. ClassType is used to decorate its scope.
        if node.kind()=='prim::GetAttr':
            assert node.scopeName() == ''

            # Since `populate_namespace_from_OP_to_IO` is already available, we just ignore this.
            # TODO: When it comes to shared parameter, will it still work?
            if " : ClassType" in  node.__repr__():
                continue

            nodes_py.append(NodePyIO(node, debugName=list(node.outputs())[0].debugName()))
            continue

        nodes_py.append(NodePyOP(node))

    nodes_py.find_common_root()
    nodes_py.populate_namespace_from_OP_to_IO()
    return nodes_py.to_proto()


def graph(model, args, verbose=False, **kwargs):
    """
    This method processes a PyTorch model and produces a `GraphDef` proto
    that can be logged to TensorBoard.

    Args:
      model (PyTorch module): The model to be parsed.
      args (tuple): input tensor[s] for the model.
      verbose (bool): Whether to print out verbose information while
        processing.
    """
    import torch

    with torch.onnx.set_training(model, False):  # TODO: move outside of torch.onnx
        try:
            trace = torch.jit.trace(model, args)
            if type(trace) == torch.jit.ScriptModule:
                graph = trace.forward_impl.graph
            else:
                graph = trace.graph

        except RuntimeError as e:
            print(e)
            print('Error occurs, No graph saved')
            raise e
            # Create an object matching
            # https://github.com/tensorflow/tensorboard/blob/master/tensorboard/compat/proto/graph.proto
            # The producer version has been reverse engineered from standard
            # TensorBoard logged data.

    if verbose:
        print(graph)
    list_of_nodes, node_stats = parse(graph, args)
    # We are hardcoding that this was run on CPU even though it might have actually
    # run on GPU. Note this is what is shown in TensorBoard and has no bearing
    # on actual execution.
    # TODO: See if we can extract GPU vs CPU information from the PyTorch model
    # and pass it correctly to TensorBoard.
    #
    # Definition of StepStats and DeviceStepStats can be found at
    # https://github.com/tensorflow/tensorboard/blob/master/tensorboard/plugins/graph/tf_graph_common/test/graph-test.ts
    # and
    # https://github.com/tensorflow/tensorboard/blob/master/tensorboard/compat/proto/step_stats.proto
    stepstats = RunMetadata(step_stats=StepStats(dev_stats=[DeviceStepStats(device="/device:CPU:0",
                                                                            node_stats=node_stats)]))
    return GraphDef(node=list_of_nodes, versions=VersionDef(producer=22)), stepstats

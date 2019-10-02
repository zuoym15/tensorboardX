# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboardX/proto/layout.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboardX/proto/layout.proto',
  package='tensorboardX',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ftensorboardX/proto/layout.proto\x12\x0ctensorboardX\"\x8f\x01\n\x05\x43hart\x12\r\n\x05title\x18\x01 \x01(\t\x12\x38\n\tmultiline\x18\x02 \x01(\x0b\x32#.tensorboardX.MultilineChartContentH\x00\x12\x32\n\x06margin\x18\x03 \x01(\x0b\x32 .tensorboardX.MarginChartContentH\x00\x42\t\n\x07\x63ontent\"$\n\x15MultilineChartContent\x12\x0b\n\x03tag\x18\x01 \x03(\t\"\x84\x01\n\x12MarginChartContent\x12\x37\n\x06series\x18\x01 \x03(\x0b\x32\'.tensorboardX.MarginChartContent.Series\x1a\x35\n\x06Series\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05lower\x18\x02 \x01(\t\x12\r\n\x05upper\x18\x03 \x01(\t\"M\n\x08\x43\x61tegory\x12\r\n\x05title\x18\x01 \x01(\t\x12\"\n\x05\x63hart\x18\x02 \x03(\x0b\x32\x13.tensorboardX.Chart\x12\x0e\n\x06\x63losed\x18\x03 \x01(\x08\"C\n\x06Layout\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12(\n\x08\x63\x61tegory\x18\x02 \x03(\x0b\x32\x16.tensorboardX.Categoryb\x06proto3')
)




_CHART = _descriptor.Descriptor(
  name='Chart',
  full_name='tensorboardX.Chart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='tensorboardX.Chart.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiline', full_name='tensorboardX.Chart.multiline', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='margin', full_name='tensorboardX.Chart.margin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='tensorboardX.Chart.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=50,
  serialized_end=193,
)


_MULTILINECHARTCONTENT = _descriptor.Descriptor(
  name='MultilineChartContent',
  full_name='tensorboardX.MultilineChartContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='tensorboardX.MultilineChartContent.tag', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=231,
)


_MARGINCHARTCONTENT_SERIES = _descriptor.Descriptor(
  name='Series',
  full_name='tensorboardX.MarginChartContent.Series',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboardX.MarginChartContent.Series.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lower', full_name='tensorboardX.MarginChartContent.Series.lower', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper', full_name='tensorboardX.MarginChartContent.Series.upper', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=366,
)

_MARGINCHARTCONTENT = _descriptor.Descriptor(
  name='MarginChartContent',
  full_name='tensorboardX.MarginChartContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='series', full_name='tensorboardX.MarginChartContent.series', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARGINCHARTCONTENT_SERIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=366,
)


_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='tensorboardX.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='tensorboardX.Category.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chart', full_name='tensorboardX.Category.chart', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closed', full_name='tensorboardX.Category.closed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=445,
)


_LAYOUT = _descriptor.Descriptor(
  name='Layout',
  full_name='tensorboardX.Layout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorboardX.Layout.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='tensorboardX.Layout.category', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=514,
)

_CHART.fields_by_name['multiline'].message_type = _MULTILINECHARTCONTENT
_CHART.fields_by_name['margin'].message_type = _MARGINCHARTCONTENT
_CHART.oneofs_by_name['content'].fields.append(
  _CHART.fields_by_name['multiline'])
_CHART.fields_by_name['multiline'].containing_oneof = _CHART.oneofs_by_name['content']
_CHART.oneofs_by_name['content'].fields.append(
  _CHART.fields_by_name['margin'])
_CHART.fields_by_name['margin'].containing_oneof = _CHART.oneofs_by_name['content']
_MARGINCHARTCONTENT_SERIES.containing_type = _MARGINCHARTCONTENT
_MARGINCHARTCONTENT.fields_by_name['series'].message_type = _MARGINCHARTCONTENT_SERIES
_CATEGORY.fields_by_name['chart'].message_type = _CHART
_LAYOUT.fields_by_name['category'].message_type = _CATEGORY
DESCRIPTOR.message_types_by_name['Chart'] = _CHART
DESCRIPTOR.message_types_by_name['MultilineChartContent'] = _MULTILINECHARTCONTENT
DESCRIPTOR.message_types_by_name['MarginChartContent'] = _MARGINCHARTCONTENT
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['Layout'] = _LAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chart = _reflection.GeneratedProtocolMessageType('Chart', (_message.Message,), {
  'DESCRIPTOR' : _CHART,
  '__module__' : 'tensorboardX.proto.layout_pb2'
  # @@protoc_insertion_point(class_scope:tensorboardX.Chart)
  })
_sym_db.RegisterMessage(Chart)

MultilineChartContent = _reflection.GeneratedProtocolMessageType('MultilineChartContent', (_message.Message,), {
  'DESCRIPTOR' : _MULTILINECHARTCONTENT,
  '__module__' : 'tensorboardX.proto.layout_pb2'
  # @@protoc_insertion_point(class_scope:tensorboardX.MultilineChartContent)
  })
_sym_db.RegisterMessage(MultilineChartContent)

MarginChartContent = _reflection.GeneratedProtocolMessageType('MarginChartContent', (_message.Message,), {

  'Series' : _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
    'DESCRIPTOR' : _MARGINCHARTCONTENT_SERIES,
    '__module__' : 'tensorboardX.proto.layout_pb2'
    # @@protoc_insertion_point(class_scope:tensorboardX.MarginChartContent.Series)
    })
  ,
  'DESCRIPTOR' : _MARGINCHARTCONTENT,
  '__module__' : 'tensorboardX.proto.layout_pb2'
  # @@protoc_insertion_point(class_scope:tensorboardX.MarginChartContent)
  })
_sym_db.RegisterMessage(MarginChartContent)
_sym_db.RegisterMessage(MarginChartContent.Series)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'tensorboardX.proto.layout_pb2'
  # @@protoc_insertion_point(class_scope:tensorboardX.Category)
  })
_sym_db.RegisterMessage(Category)

Layout = _reflection.GeneratedProtocolMessageType('Layout', (_message.Message,), {
  'DESCRIPTOR' : _LAYOUT,
  '__module__' : 'tensorboardX.proto.layout_pb2'
  # @@protoc_insertion_point(class_scope:tensorboardX.Layout)
  })
_sym_db.RegisterMessage(Layout)


# @@protoc_insertion_point(module_scope)

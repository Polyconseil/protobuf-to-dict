# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='sample.proto',
  package='tests',
  serialized_pb=b'\n\x0csample.proto\x12\x05tests\"\xf5\x03\n\x0eMessageOfTypes\x12\x0c\n\x04\x64ubl\x18\x01 \x02(\x01\x12\x0c\n\x04\x66lot\x18\x02 \x02(\x02\x12\x0b\n\x03i32\x18\x03 \x02(\x05\x12\x0b\n\x03i64\x18\x04 \x02(\x03\x12\x0c\n\x04ui32\x18\x05 \x02(\r\x12\x0c\n\x04ui64\x18\x06 \x02(\x04\x12\x0c\n\x04si32\x18\x07 \x02(\x11\x12\x0c\n\x04si64\x18\x08 \x02(\x12\x12\x0b\n\x03\x66\x33\x32\x18\t \x02(\x07\x12\x0b\n\x03\x66\x36\x34\x18\x11 \x02(\x06\x12\x0c\n\x04sf32\x18\n \x02(\x0f\x12\x0c\n\x04sf64\x18\x0b \x02(\x10\x12\x0b\n\x03\x62ol\x18\x0c \x02(\x08\x12\r\n\x05strng\x18\r \x02(\t\x12\x0c\n\x04\x62yts\x18\x0e \x02(\x0c\x12\x30\n\x06nested\x18\x0f \x02(\x0b\x32 .tests.MessageOfTypes.NestedType\x12\'\n\x03\x65nm\x18\x10 \x02(\x0e\x32\x1a.tests.MessageOfTypes.Enum\x12\r\n\x05range\x18\x12 \x03(\x05\x12\x38\n\x0enestedRepeated\x18\x13 \x03(\x0b\x32 .tests.MessageOfTypes.NestedType\x12/\n\x0b\x65nmRepeated\x18\x14 \x03(\x0e\x32\x1a.tests.MessageOfTypes.Enum\x1a\x19\n\nNestedType\x12\x0b\n\x03req\x18\x01 \x02(\t\"\x1b\n\x04\x45num\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x12\x05\n\x01\x43\x10\x02*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x84\x01\n\x0fNestedExtension2%\n\x06\x65xtInt\x12\x15.tests.MessageOfTypes\x18\x66 \x01(\x05\x32J\n\textNested\x12\x15.tests.MessageOfTypes\x18g \x01(\x0b\x32 .tests.MessageOfTypes.NestedType:(\n\textDouble\x12\x15.tests.MessageOfTypes\x18\x64 \x01(\x01:(\n\textString\x12\x15.tests.MessageOfTypes\x18\x65 \x01(\t')


EXTDOUBLE_FIELD_NUMBER = 100
extDouble = descriptor.FieldDescriptor(
  name='extDouble', full_name='tests.extDouble', index=0,
  number=100, type=1, cpp_type=5, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
EXTSTRING_FIELD_NUMBER = 101
extString = descriptor.FieldDescriptor(
  name='extString', full_name='tests.extString', index=1,
  number=101, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode("utf-8"),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_MESSAGEOFTYPES_ENUM = descriptor.EnumDescriptor(
  name='Enum',
  full_name='tests.MessageOfTypes.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='B', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='C', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=488,
  serialized_end=515,
)


_MESSAGEOFTYPES_NESTEDTYPE = descriptor.Descriptor(
  name='NestedType',
  full_name='tests.MessageOfTypes.NestedType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='req', full_name='tests.MessageOfTypes.NestedType.req', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=461,
  serialized_end=486,
)

_MESSAGEOFTYPES = descriptor.Descriptor(
  name='MessageOfTypes',
  full_name='tests.MessageOfTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dubl', full_name='tests.MessageOfTypes.dubl', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='flot', full_name='tests.MessageOfTypes.flot', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='i32', full_name='tests.MessageOfTypes.i32', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='i64', full_name='tests.MessageOfTypes.i64', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ui32', full_name='tests.MessageOfTypes.ui32', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ui64', full_name='tests.MessageOfTypes.ui64', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='si32', full_name='tests.MessageOfTypes.si32', index=6,
      number=7, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='si64', full_name='tests.MessageOfTypes.si64', index=7,
      number=8, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='f32', full_name='tests.MessageOfTypes.f32', index=8,
      number=9, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='f64', full_name='tests.MessageOfTypes.f64', index=9,
      number=17, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sf32', full_name='tests.MessageOfTypes.sf32', index=10,
      number=10, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sf64', full_name='tests.MessageOfTypes.sf64', index=11,
      number=11, type=16, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bol', full_name='tests.MessageOfTypes.bol', index=12,
      number=12, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strng', full_name='tests.MessageOfTypes.strng', index=13,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='byts', full_name='tests.MessageOfTypes.byts', index=14,
      number=14, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nested', full_name='tests.MessageOfTypes.nested', index=15,
      number=15, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enm', full_name='tests.MessageOfTypes.enm', index=16,
      number=16, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='range', full_name='tests.MessageOfTypes.range', index=17,
      number=18, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nestedRepeated', full_name='tests.MessageOfTypes.nestedRepeated', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enmRepeated', full_name='tests.MessageOfTypes.enmRepeated', index=19,
      number=20, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGEOFTYPES_NESTEDTYPE, ],
  enum_types=[
    _MESSAGEOFTYPES_ENUM,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(100, 536870912), ],
  serialized_start=24,
  serialized_end=525,
)


_NESTEDEXTENSION = descriptor.Descriptor(
  name='NestedExtension',
  full_name='tests.NestedExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    descriptor.FieldDescriptor(
      name='extInt', full_name='tests.NestedExtension.extInt', index=0,
      number=102, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extNested', full_name='tests.NestedExtension.extNested', index=1,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=528,
  serialized_end=660,
)

_MESSAGEOFTYPES_NESTEDTYPE.containing_type = _MESSAGEOFTYPES;
_MESSAGEOFTYPES.fields_by_name['nested'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
_MESSAGEOFTYPES.fields_by_name['enm'].enum_type = _MESSAGEOFTYPES_ENUM
_MESSAGEOFTYPES.fields_by_name['nestedRepeated'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
_MESSAGEOFTYPES.fields_by_name['enmRepeated'].enum_type = _MESSAGEOFTYPES_ENUM
_MESSAGEOFTYPES_ENUM.containing_type = _MESSAGEOFTYPES;
DESCRIPTOR.message_types_by_name['MessageOfTypes'] = _MESSAGEOFTYPES
DESCRIPTOR.message_types_by_name['NestedExtension'] = _NESTEDEXTENSION

MessageOfTypes = reflection.GeneratedProtocolMessageType('MessageOfTypes', (message.Message,),
    {
      'DESCRIPTOR': _MESSAGEOFTYPES,
      'NestedType': reflection.GeneratedProtocolMessageType('NestedType', (message.Message,),
          {
            'DESCRIPTOR': _MESSAGEOFTYPES_NESTEDTYPE,
            # @@protoc_insertion_point(class_scope:tests.MessageOfTypes.NestedType)
          }),
      # @@protoc_insertion_point(class_scope:tests.MessageOfTypes)
    })

NestedExtension = reflection.GeneratedProtocolMessageType('NestedExtension', (message.Message,),
    {
      'DESCRIPTOR': _NESTEDEXTENSION,
      # @@protoc_insertion_point(class_scope:tests.NestedExtension)
    })

MessageOfTypes.RegisterExtension(extDouble)
MessageOfTypes.RegisterExtension(extString)
MessageOfTypes.RegisterExtension(_NESTEDEXTENSION.extensions_by_name['extInt'])
_NESTEDEXTENSION.extensions_by_name['extNested'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
MessageOfTypes.RegisterExtension(_NESTEDEXTENSION.extensions_by_name['extNested'])
# @@protoc_insertion_point(module_scope)

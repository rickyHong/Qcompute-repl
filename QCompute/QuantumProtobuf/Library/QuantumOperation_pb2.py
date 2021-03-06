# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QuantumOperation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Complex_pb2 as Complex__pb2

from Complex_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='QuantumOperation.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16QuantumOperation.proto\x1a\rComplex.proto\")\n\x0e\x43ustomizedGate\x12\x17\n\x06matrix\x18\x01 \x01(\x0b\x32\x07.Matrix\"\x90\x01\n\x07Measure\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.Measure.Type\x12\r\n\x05\x63Regs\x18\x02 \x03(\r\"Y\n\x04Type\x12\x18\n\x14MeasureTypeUndefined\x10\x00\x12\x05\n\x01X\x10\x01\x12\x05\n\x01Y\x10\x02\x12\x05\n\x01Z\x10\x03\x12\n\n\x06PauliX\x10\x04\x12\n\n\x06PauliY\x10\x05\x12\n\n\x06PauliZ\x10\x06*\xa5\x01\n\tFixedGate\x12\x16\n\x12\x46ixedGateUndefined\x10\x00\x12\x06\n\x02ID\x10\x01\x12\x05\n\x01X\x10\x02\x12\x05\n\x01Y\x10\x03\x12\x05\n\x01Z\x10\x04\x12\x05\n\x01H\x10\x05\x12\x05\n\x01S\x10\x06\x12\x07\n\x03SDG\x10\x07\x12\x05\n\x01T\x10\x08\x12\x07\n\x03TDG\x10\t\x12\x06\n\x02\x43X\x10\n\x12\x06\n\x02\x43Y\x10\x0b\x12\x06\n\x02\x43Z\x10\x0c\x12\x06\n\x02\x43H\x10\r\x12\x08\n\x04SWAP\x10\x0e\x12\x07\n\x03\x43\x43X\x10\x0f\x12\t\n\x05\x43SWAP\x10\x10*k\n\x0cRotationGate\x12\x19\n\x15RotationGateUndefined\x10\x00\x12\x05\n\x01U\x10\x01\x12\x06\n\x02RX\x10\x02\x12\x06\n\x02RY\x10\x03\x12\x06\n\x02RZ\x10\x04\x12\x06\n\x02\x43U\x10\x05\x12\x07\n\x03\x43RX\x10\x06\x12\x07\n\x03\x43RY\x10\x07\x12\x07\n\x03\x43RZ\x10\x08*4\n\rCompositeGate\x12\x1a\n\x16\x43ompositeGateUndefined\x10\x00\x12\x07\n\x03RZZ\x10\x01P\x00\x62\x06proto3'
  ,
  dependencies=[Complex__pb2.DESCRIPTOR,],
  public_dependencies=[Complex__pb2.DESCRIPTOR,])

_FIXEDGATE = _descriptor.EnumDescriptor(
  name='FixedGate',
  full_name='FixedGate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FixedGateUndefined', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ID', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='X', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Y', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Z', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='H', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='S', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SDG', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='T', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TDG', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CX', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CY', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CZ', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CH', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SWAP', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CCX', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CSWAP', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=232,
  serialized_end=397,
)
_sym_db.RegisterEnumDescriptor(_FIXEDGATE)

FixedGate = enum_type_wrapper.EnumTypeWrapper(_FIXEDGATE)
_ROTATIONGATE = _descriptor.EnumDescriptor(
  name='RotationGate',
  full_name='RotationGate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RotationGateUndefined', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='U', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RZ', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CU', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRX', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRZ', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=399,
  serialized_end=506,
)
_sym_db.RegisterEnumDescriptor(_ROTATIONGATE)

RotationGate = enum_type_wrapper.EnumTypeWrapper(_ROTATIONGATE)
_COMPOSITEGATE = _descriptor.EnumDescriptor(
  name='CompositeGate',
  full_name='CompositeGate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CompositeGateUndefined', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RZZ', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=508,
  serialized_end=560,
)
_sym_db.RegisterEnumDescriptor(_COMPOSITEGATE)

CompositeGate = enum_type_wrapper.EnumTypeWrapper(_COMPOSITEGATE)
FixedGateUndefined = 0
ID = 1
X = 2
Y = 3
Z = 4
H = 5
S = 6
SDG = 7
T = 8
TDG = 9
CX = 10
CY = 11
CZ = 12
CH = 13
SWAP = 14
CCX = 15
CSWAP = 16
RotationGateUndefined = 0
U = 1
RX = 2
RY = 3
RZ = 4
CU = 5
CRX = 6
CRY = 7
CRZ = 8
CompositeGateUndefined = 0
RZZ = 1


_MEASURE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Measure.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MeasureTypeUndefined', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='X', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Y', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Z', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PauliX', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PauliY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PauliZ', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=140,
  serialized_end=229,
)
_sym_db.RegisterEnumDescriptor(_MEASURE_TYPE)


_CUSTOMIZEDGATE = _descriptor.Descriptor(
  name='CustomizedGate',
  full_name='CustomizedGate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matrix', full_name='CustomizedGate.matrix', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=41,
  serialized_end=82,
)


_MEASURE = _descriptor.Descriptor(
  name='Measure',
  full_name='Measure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Measure.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cRegs', full_name='Measure.cRegs', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEASURE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=229,
)

_CUSTOMIZEDGATE.fields_by_name['matrix'].message_type = Complex__pb2._MATRIX
_MEASURE.fields_by_name['type'].enum_type = _MEASURE_TYPE
_MEASURE_TYPE.containing_type = _MEASURE
DESCRIPTOR.message_types_by_name['CustomizedGate'] = _CUSTOMIZEDGATE
DESCRIPTOR.message_types_by_name['Measure'] = _MEASURE
DESCRIPTOR.enum_types_by_name['FixedGate'] = _FIXEDGATE
DESCRIPTOR.enum_types_by_name['RotationGate'] = _ROTATIONGATE
DESCRIPTOR.enum_types_by_name['CompositeGate'] = _COMPOSITEGATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomizedGate = _reflection.GeneratedProtocolMessageType('CustomizedGate', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMIZEDGATE,
  '__module__' : 'QuantumOperation_pb2'
  # @@protoc_insertion_point(class_scope:CustomizedGate)
  })
_sym_db.RegisterMessage(CustomizedGate)

Measure = _reflection.GeneratedProtocolMessageType('Measure', (_message.Message,), {
  'DESCRIPTOR' : _MEASURE,
  '__module__' : 'QuantumOperation_pb2'
  # @@protoc_insertion_point(class_scope:Measure)
  })
_sym_db.RegisterMessage(Measure)


# @@protoc_insertion_point(module_scope)

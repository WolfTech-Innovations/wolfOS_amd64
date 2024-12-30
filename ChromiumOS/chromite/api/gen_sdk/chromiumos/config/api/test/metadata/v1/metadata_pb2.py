# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/metadata/v1/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.dut.v1 import dut_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_dut_dot_v1_dot_dut__pb2
from chromite.api.gen_sdk.chromiumos.config.api import hardware_topology_pb2 as chromiumos_dot_config_dot_api_dot_hardware__topology__pb2
from chromite.api.gen_sdk.chromiumos.config.api import topology_pb2 as chromiumos_dot_config_dot_api_dot_topology__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5chromiumos/config/api/test/metadata/v1/metadata.proto\x12&chromiumos.config.api.test.metadata.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a+chromiumos/config/api/test/dut/v1/dut.proto\x1a-chromiumos/config/api/hardware_topology.proto\x1a$chromiumos/config/api/topology.proto\"f\n\rSpecification\x12U\n\x13remote_test_drivers\x18\x01 \x03(\x0b\x32\x38.chromiumos.config.api.test.metadata.v1.RemoteTestDriver\"\xc6\x01\n\x10RemoteTestDriver\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x0c\x64ocker_image\x18\x05 \x01(\x0b\x32\x33.chromiumos.config.api.test.metadata.v1.DockerImage\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\t\x12;\n\x05tests\x18\x04 \x03(\x0b\x32,.chromiumos.config.api.test.metadata.v1.TestJ\x04\x08\x02\x10\x03R\x05image\"\x1d\n\x0b\x44ockerImage\x12\x0e\n\x06\x64igest\x18\x01 \x01(\t\"\xdb\x02\n\x04Test\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\nattributes\x18\x02 \x03(\x0b\x32\x31.chromiumos.config.api.test.metadata.v1.Attribute\x12M\n\x0e\x64ut_constraint\x18\x06 \x01(\x0b\x32\x35.chromiumos.config.api.test.metadata.v1.DUTConstraint\x12L\n\rinformational\x18\x04 \x01(\x0b\x32\x35.chromiumos.config.api.test.metadata.v1.Informational\x12O\n\rdut_condition\x18\x05 \x01(\x0b\x32\x34.chromiumos.config.api.test.metadata.v1.DUTConditionB\x02\x18\x01J\x04\x08\x03\x10\x04R\nconditions\"\x19\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa7\x01\n\rDUTConstraint\x12K\n\x06\x63onfig\x18\x01 \x01(\x0b\x32;.chromiumos.config.api.test.metadata.v1.DUTConfigConstraint\x12I\n\x05setup\x18\x02 \x01(\x0b\x32:.chromiumos.config.api.test.metadata.v1.DUTSetupConstraint\"t\n\x13\x44UTConfigConstraint\x12\x12\n\nexpression\x18\x01 \x01(\t\x1aI\n\x03\x44UT\x12\x42\n\x11hardware_features\x18\x01 \x01(\x0b\x32\'.chromiumos.config.api.HardwareFeatures\"r\n\x12\x44UTSetupConstraint\x12\x12\n\nexpression\x18\x01 \x01(\t\x1aH\n\x03\x44UT\x12\x41\n\x05setup\x18\x01 \x01(\x0b\x32\x32.chromiumos.config.api.test.dut.v1.DeviceUnderTest\"\xf7\x01\n\x0c\x44UTCondition\x12\x12\n\nexpression\x18\x01 \x01(\t\x1a\xd2\x01\n\x05Scope\x12\x41\n\x05setup\x18\x01 \x01(\x0b\x32\x32.chromiumos.config.api.test.dut.v1.DeviceUnderTest\x12\x42\n\x11hardware_topology\x18\x02 \x01(\x0b\x32\'.chromiumos.config.api.HardwareTopology\x12\x42\n\x11hardware_features\x18\x03 \x01(\x0b\x32\'.chromiumos.config.api.HardwareFeatures\"{\n\rInformational\x12@\n\x07\x61uthors\x18\x01 \x03(\x0b\x32/.chromiumos.config.api.test.metadata.v1.Contact\x12(\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"7\n\x07\x43ontact\x12\x0f\n\x05\x65mail\x18\x01 \x01(\tH\x00\x12\x13\n\tmdb_group\x18\x02 \x01(\tH\x00\x42\x06\n\x04typeBSB\rMetadataProtoZBgo.chromium.org/chromiumos/config/go/api/test/metadata/v1;metadatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.config.api.test.metadata.v1.metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\rMetadataProtoZBgo.chromium.org/chromiumos/config/go/api/test/metadata/v1;metadata'
  _TEST.fields_by_name['dut_condition']._options = None
  _TEST.fields_by_name['dut_condition']._serialized_options = b'\030\001'
  _globals['_SPECIFICATION']._serialized_start=257
  _globals['_SPECIFICATION']._serialized_end=359
  _globals['_REMOTETESTDRIVER']._serialized_start=362
  _globals['_REMOTETESTDRIVER']._serialized_end=560
  _globals['_DOCKERIMAGE']._serialized_start=562
  _globals['_DOCKERIMAGE']._serialized_end=591
  _globals['_TEST']._serialized_start=594
  _globals['_TEST']._serialized_end=941
  _globals['_ATTRIBUTE']._serialized_start=943
  _globals['_ATTRIBUTE']._serialized_end=968
  _globals['_DUTCONSTRAINT']._serialized_start=971
  _globals['_DUTCONSTRAINT']._serialized_end=1138
  _globals['_DUTCONFIGCONSTRAINT']._serialized_start=1140
  _globals['_DUTCONFIGCONSTRAINT']._serialized_end=1256
  _globals['_DUTCONFIGCONSTRAINT_DUT']._serialized_start=1183
  _globals['_DUTCONFIGCONSTRAINT_DUT']._serialized_end=1256
  _globals['_DUTSETUPCONSTRAINT']._serialized_start=1258
  _globals['_DUTSETUPCONSTRAINT']._serialized_end=1372
  _globals['_DUTSETUPCONSTRAINT_DUT']._serialized_start=1300
  _globals['_DUTSETUPCONSTRAINT_DUT']._serialized_end=1372
  _globals['_DUTCONDITION']._serialized_start=1375
  _globals['_DUTCONDITION']._serialized_end=1622
  _globals['_DUTCONDITION_SCOPE']._serialized_start=1412
  _globals['_DUTCONDITION_SCOPE']._serialized_end=1622
  _globals['_INFORMATIONAL']._serialized_start=1624
  _globals['_INFORMATIONAL']._serialized_end=1747
  _globals['_CONTACT']._serialized_start=1749
  _globals['_CONTACT']._serialized_end=1804
# @@protoc_insertion_point(module_scope)
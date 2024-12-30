# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/plan/v1/plan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-chromiumos/config/api/test/plan/v1/plan.proto\x12\"chromiumos.config.api.test.plan.v1\"H\n\rSpecification\x12\x37\n\x05plans\x18\x01 \x03(\x0b\x32(.chromiumos.config.api.test.plan.v1.Plan\"M\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x05units\x18\x02 \x03(\x0b\x32(.chromiumos.config.api.test.plan.v1.Unit\"1\n\x0c\x44utCriterion\x12\x11\n\tattribute\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"\xa6\x01\n\x0c\x43overageRule\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x46\n\x0c\x64ut_criteria\x18\x02 \x03(\x0b\x32\x30.chromiumos.config.api.test.plan.v1.DutCriterion\x12@\n\texclusion\x18\x04 \x01(\x0b\x32-.chromiumos.config.api.test.plan.v1.Exclusion\"\xdf\x02\n\x04Unit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x06suites\x18\x02 \x03(\x0b\x32..chromiumos.config.api.test.plan.v1.Unit.Suite\x12<\n\x05tests\x18\x03 \x03(\x0b\x32-.chromiumos.config.api.test.plan.v1.Unit.Test\x12H\n\x0e\x63overage_rules\x18\x04 \x03(\x0b\x32\x30.chromiumos.config.api.test.plan.v1.CoverageRule\x12@\n\texclusion\x18\x05 \x01(\x0b\x32-.chromiumos.config.api.test.plan.v1.Exclusion\x1a\x15\n\x05Suite\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a(\n\x04Test\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nattributes\x18\x02 \x03(\t\"\xaf\x03\n\tExclusion\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.chromiumos.config.api.test.plan.v1.Exclusion.Type\x12\x44\n\x06\x61\x63tion\x18\x05 \x01(\x0e\x32\x34.chromiumos.config.api.test.plan.v1.Exclusion.Action\x12\x12\n\nreferences\x18\x04 \x03(\t\"\xb7\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tPERMANENT\x10\x01\x12\x16\n\x12TEMPORARY_NEW_TEST\x10\x02\x12\x19\n\x15TEMPORARY_PENDING_FIX\x10\x03\x12%\n!TEMPORARY_NO_LAB_DEVICES_DEPLOYED\x10\x04\x12\x30\n,TEMPORARY_INSUFFICIENT_LAB_DEVICES_AVAILABLE\x10\x05\"L\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x44O_NOT_SCHEDULE\x10\x01\x12\x15\n\x11MARK_NON_CRITICAL\x10\x02\x42<Z:go.chromium.org/chromiumos/config/go/api/test/plan/v1;planb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.config.api.test.plan.v1.plan_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:go.chromium.org/chromiumos/config/go/api/test/plan/v1;plan'
  _globals['_SPECIFICATION']._serialized_start=85
  _globals['_SPECIFICATION']._serialized_end=157
  _globals['_PLAN']._serialized_start=159
  _globals['_PLAN']._serialized_end=236
  _globals['_DUTCRITERION']._serialized_start=238
  _globals['_DUTCRITERION']._serialized_end=287
  _globals['_COVERAGERULE']._serialized_start=290
  _globals['_COVERAGERULE']._serialized_end=456
  _globals['_UNIT']._serialized_start=459
  _globals['_UNIT']._serialized_end=810
  _globals['_UNIT_SUITE']._serialized_start=747
  _globals['_UNIT_SUITE']._serialized_end=768
  _globals['_UNIT_TEST']._serialized_start=770
  _globals['_UNIT_TEST']._serialized_end=810
  _globals['_EXCLUSION']._serialized_start=813
  _globals['_EXCLUSION']._serialized_end=1244
  _globals['_EXCLUSION_TYPE']._serialized_start=983
  _globals['_EXCLUSION_TYPE']._serialized_end=1166
  _globals['_EXCLUSION_ACTION']._serialized_start=1168
  _globals['_EXCLUSION_ACTION']._serialized_end=1244
# @@protoc_insertion_point(module_scope)
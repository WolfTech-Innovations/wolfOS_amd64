# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/scheduling/task_request_event.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf.internal import builder as _builder
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import descriptor_pool as _descriptor_pool
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromiumos.test.scheduling import os_type_pb2 as chromiumos_dot_test_dot_scheduling_dot_os__type__pb2
from chromite.api.gen.chromiumos.test.scheduling import swarming_dimensions_pb2 as chromiumos_dot_test_dot_scheduling_dot_swarming__dimensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3chromiumos/test/scheduling/task_request_event.proto\x12\x1a\x63hromiumos.test.scheduling\x1a(chromiumos/test/scheduling/os_type.proto\x1a\x34\x63hromiumos/test/scheduling/swarming_dimensions.proto\"\xd0\x03\n\x10TaskRequestEvent\x12\x12\n\nevent_time\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x65\x61\x64line\x18\x02 \x01(\x03\x12\x10\n\x08periodic\x18\x03 \x01(\x08\x12\x10\n\x08priority\x18\x04 \x01(\x03\x12L\n\x14requested_dimensions\x18\x05 \x01(\x0b\x32..chromiumos.test.scheduling.SwarmingDimensions\x12\x1e\n\x16real_execution_minutes\x18\x06 \x01(\x03\x12\x1d\n\x15max_execution_minutes\x18\x07 \x01(\x03\x12#\n\x1bschedule_build_request_json\x18\x08 \x01(\t\x12\x12\n\nqs_account\x18\t \x01(\t\x12\x0c\n\x04pool\x18\n \x01(\t\x12\x0c\n\x04\x62\x62id\x18\x0b \x01(\x03\x12\x0c\n\x04\x61sap\x18\x0c \x01(\x08\x12\x15\n\rtask_state_id\x18\r \x01(\x03\x12\x13\n\x0b\x64\x65vice_name\x18\x0e \x01(\t\x12\x0c\n\x04user\x18\x0f \x01(\t\x12\x13\n\x0b\x65xperiments\x18\x10 \x03(\t\x12\x33\n\x07os_type\x18\x11 \x01(\x0e\x32\".chromiumos.test.scheduling.OsType\"Q\n\x11TaskRequestEvents\x12<\n\x06\x65vents\x18\x01 \x03(\x0b\x32,.chromiumos.test.scheduling.TaskRequestEvent\"\xc5\x01\n\x16KeyedTaskRequestEvents\x12N\n\x06\x65vents\x18\x01 \x03(\x0b\x32>.chromiumos.test.scheduling.KeyedTaskRequestEvents.EventsEntry\x1a[\n\x0b\x45ventsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.chromiumos.test.scheduling.TaskRequestEvent:\x02\x38\x01\x42\tZ\x07./protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.test.scheduling.task_request_event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007./proto'
  _KEYEDTASKREQUESTEVENTS_EVENTSENTRY._options = None
  _KEYEDTASKREQUESTEVENTS_EVENTSENTRY._serialized_options = b'8\001'
  _TASKREQUESTEVENT._serialized_start=180
  _TASKREQUESTEVENT._serialized_end=644
  _TASKREQUESTEVENTS._serialized_start=646
  _TASKREQUESTEVENTS._serialized_end=727
  _KEYEDTASKREQUESTEVENTS._serialized_start=730
  _KEYEDTASKREQUESTEVENTS._serialized_end=927
  _KEYEDTASKREQUESTEVENTS_EVENTSENTRY._serialized_start=836
  _KEYEDTASKREQUESTEVENTS_EVENTSENTRY._serialized_end=927
# @@protoc_insertion_point(module_scope)
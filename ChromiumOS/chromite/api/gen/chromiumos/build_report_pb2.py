# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/build_report.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf.internal import builder as _builder
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import descriptor_pool as _descriptor_pool
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from chromite.third_party.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63hromiumos/build_report.proto\x12\nchromiumos\x1a\x17\x63hromiumos/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"_\n\tTimeframe\x12)\n\x05\x62\x65gin\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\")\n\x07\x42uildId\x12\x18\n\x0e\x62uildbucket_id\x18\x01 \x01(\x03H\x00\x42\x04\n\x02id\"\x1b\n\x03URI\x12\r\n\x03gcs\x18\x01 \x01(\tH\x00\x42\x05\n\x03uri\"G\n\x0b\x44lcArtifact\x12\x1c\n\x03uri\x18\x01 \x01(\x0b\x32\x0f.chromiumos.URI\x12\x0e\n\x06sha256\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\"\xa2*\n\x0b\x42uildReport\x12\x18\n\x0e\x62uildbucket_id\x18\x01 \x01(\x03H\x00\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12#\n\x06parent\x18\t \x01(\x0b\x32\x13.chromiumos.BuildId\x12%\n\x08\x63hildren\x18\n \x03(\x0b\x32\x13.chromiumos.BuildId\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.chromiumos.BuildReport.BuildType\x12\x33\n\x06status\x18\x03 \x01(\x0b\x32#.chromiumos.BuildReport.BuildStatus\x12\x33\n\x06\x63onfig\x18\x04 \x01(\x0b\x32#.chromiumos.BuildReport.BuildConfig\x12\x32\n\x05steps\x18\x05 \x01(\x0b\x32#.chromiumos.BuildReport.StepDetails\x12\x42\n\rsigned_builds\x18\x06 \x03(\x0b\x32+.chromiumos.BuildReport.SignedBuildMetadata\x12\x1a\n\x12signing_was_mocked\x18\x0c \x01(\x08\x12\x31\n\x08payloads\x18\x0b \x03(\x0b\x32\x1f.chromiumos.BuildReport.Payload\x12\x13\n\x0bsdk_version\x18\r \x01(\t\x12\x15\n\rtoolchain_url\x18\x0e \x01(\t\x12\x12\n\ntoolchains\x18\x0f \x03(\t\x12\x12\n\nsdk_bucket\x18\x11 \x01(\t\x12\x38\n\tartifacts\x18\x07 \x03(\x0b\x32%.chromiumos.BuildReport.BuildArtifact\x12*\n\x04\x64lcs\x18\x10 \x01(\x0b\x32\x1c.chromiumos.BuildReport.DLCs\x1a\xec\x01\n\x0b\x42uildStatus\x12\x39\n\x05value\x18\x01 \x01(\x0e\x32*.chromiumos.BuildReport.BuildStatus.Status\"\xa1\x01\n\x06Status\x12\r\n\tUNDEFINED\x10\x00\x12\x11\n\rKIND_TERMINAL\x10\x01\x12\x10\n\x0cKIND_RUNNING\x10\x02\x12\x0b\n\x07SUCCESS\x10\x64\x12\x0b\n\x07\x46\x41ILURE\x10\x65\x12\x11\n\rINFRA_FAILURE\x10\x66\x12\x0c\n\x08WATCHDOG\x10g\x12\x0c\n\x08\x43\x41NCELED\x10h\x12\x0c\n\x07RUNNING\x10\xc8\x01\x12\x0c\n\x07WAITING\x10\xc9\x01\x1a\x8f\x0b\n\x0b\x42uildConfig\x12:\n\x06\x62ranch\x18\x01 \x01(\x0b\x32*.chromiumos.BuildReport.BuildConfig.Branch\x12L\n\x18\x61ndroid_container_branch\x18\x02 \x01(\x0b\x32*.chromiumos.BuildReport.BuildConfig.Branch\x12:\n\x06target\x18\x03 \x01(\x0b\x32*.chromiumos.BuildReport.BuildConfig.Target\x12L\n\x18\x61ndroid_container_target\x18\x04 \x01(\x0b\x32*.chromiumos.BuildReport.BuildConfig.Target\x12<\n\x07release\x18\x05 \x01(\x0b\x32+.chromiumos.BuildReport.BuildConfig.Release\x12=\n\x08versions\x18\x06 \x03(\x0b\x32+.chromiumos.BuildReport.BuildConfig.Version\x12\x13\n\x0b\x61rc_use_set\x18\x07 \x01(\x08\x12\x39\n\x06models\x18\x08 \x03(\x0b\x32).chromiumos.BuildReport.BuildConfig.Model\x1a\x9b\x03\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x66irmware_key_id\x18\x02 \x01(\t\x12H\n\x08versions\x18\x03 \x03(\x0b\x32\x36.chromiumos.BuildReport.BuildConfig.Model.ModelVersion\x1ag\n\x0cModelVersion\x12H\n\x04kind\x18\x01 \x01(\x0e\x32:.chromiumos.BuildReport.BuildConfig.Model.ModelVersionKind\x12\r\n\x05value\x18\x02 \x01(\t\"\xb7\x01\n\x10ModelVersionKind\x12 \n\x1cMODEL_VERSION_KIND_UNDEFINED\x10\x00\x12\"\n\x1eMODEL_VERSION_KIND_EC_FIRMWARE\x10\x01\x12-\n)MODEL_VERSION_KIND_MAIN_READONLY_FIRMWARE\x10\x02\x12.\n*MODEL_VERSION_KIND_MAIN_READWRITE_FIRMWARE\x10\x03\x1a\x30\n\x07Release\x12%\n\x08\x63hannels\x18\x01 \x03(\x0e\x32\x13.chromiumos.Channel\x1a\x16\n\x06\x42ranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x1aW\n\x07Version\x12=\n\x04kind\x18\x01 \x01(\x0e\x32/.chromiumos.BuildReport.BuildConfig.VersionKind\x12\r\n\x05value\x18\x02 \x01(\t\x1a\x16\n\x06Target\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xc5\x02\n\x0bVersionKind\x12\x1a\n\x16VERSION_KIND_UNDEFINED\x10\x00\x12\x1b\n\x17VERSION_KIND_ASH_CHROME\x10\x01\x12\x17\n\x13VERSION_KIND_CHROME\x10\x02\x12\x14\n\x10VERSION_KIND_ARC\x10\x03\x12\x19\n\x15VERSION_KIND_PLATFORM\x10\x04\x12\x1a\n\x16VERSION_KIND_MILESTONE\x10\x05\x12\"\n\x1eVERSION_KIND_ANDROID_CONTAINER\x10\x06\x12\x1c\n\x18VERSION_KIND_EC_FIRMWARE\x10\x07\x12\x1c\n\x18VERSION_KIND_FINGERPRINT\x10\x08\x12\x17\n\x13VERSION_KIND_KERNEL\x10\t\x12\x1e\n\x1aVERSION_KIND_MAIN_FIRMWARE\x10\n\x1a\xb0\x03\n\rBuildArtifact\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.chromiumos.BuildReport.BuildArtifact.Type\x12\x1c\n\x03uri\x18\x02 \x01(\x0b\x32\x0f.chromiumos.URI\x12\x0e\n\x06sha256\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x03\x12+\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xfb\x01\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tIMAGE_ZIP\x10\x01\x12\x15\n\x11\x46\x41\x43TORY_IMAGE_ZIP\x10\x02\x12\x1a\n\x16\x46IRMWARE_IMAGE_ARCHIVE\x10\x03\x12\x16\n\x12TEST_IMAGE_ARCHIVE\x10\x04\x12\x1d\n\x19\x46IRMWARE_AP_IMAGE_ARCHIVE\x10\x05\x12\x1d\n\x19\x46IRMWARE_EC_IMAGE_ARCHIVE\x10\x06\x12\x12\n\x0eHWQUAL_ARCHIVE\x10\x65\x12\x11\n\rDEBUG_ARCHIVE\x10\x66\x12\x11\n\x0cPAYLOAD_FULL\x10\x90\x03\x12\x12\n\rPAYLOAD_DELTA\x10\x91\x03\x1a\xb5\x06\n\x0bStepDetails\x12=\n\x07\x63urrent\x18\x01 \x01(\x0e\x32,.chromiumos.BuildReport.StepDetails.StepName\x12;\n\x04info\x18\x02 \x03(\x0b\x32-.chromiumos.BuildReport.StepDetails.InfoEntry\x1a}\n\x08StepInfo\x12\r\n\x05order\x18\x01 \x01(\x05\x12:\n\x06status\x18\x02 \x01(\x0e\x32*.chromiumos.BuildReport.StepDetails.Status\x12&\n\x07runtime\x18\x03 \x01(\x0b\x32\x15.chromiumos.Timeframe\x1aY\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.chromiumos.BuildReport.StepDetails.StepInfo:\x02\x38\x01\"\xc9\x01\n\x06Status\x12\x19\n\x15STEP_STATUS_UNDEFINED\x10\x00\x12\x11\n\rKIND_TERMINAL\x10\x01\x12\x10\n\x0cKIND_RUNNING\x10\x02\x12\x12\n\x0eSTATUS_SUCCESS\x10\x64\x12\x12\n\x0eSTATUS_FAILURE\x10\x65\x12\x18\n\x14STATUS_INFRA_FAILURE\x10\x66\x12\x13\n\x0fSTATUS_WATCHDOG\x10g\x12\x13\n\x0fSTATUS_CANCELED\x10h\x12\x13\n\x0eSTATUS_RUNNING\x10\xc8\x01\"\x83\x02\n\x08StepName\x12\x12\n\x0eSTEP_UNDEFINED\x10\x00\x12\x10\n\x0cSTEP_OVERALL\x10\x64\x12\x0e\n\tSTEP_SYNC\x10\xc8\x01\x12\x15\n\x10STEP_SYNC_CHROME\x10\xc9\x01\x12\r\n\x08STEP_SDK\x10\xac\x02\x12\x12\n\rSTEP_SDK_INIT\x10\xad\x02\x12\x14\n\x0fSTEP_SDK_UPDATE\x10\xae\x02\x12\x0f\n\nSTEP_BUILD\x10\x90\x03\x12\x17\n\x12STEP_BUILD_SYSROOT\x10\x91\x03\x12\x18\n\x13STEP_BUILD_PACKAGES\x10\x92\x03\x12\x17\n\x12STEP_DEBUG_SYMBOLS\x10\xf4\x03\x12\x14\n\x0fSTEP_UNIT_TESTS\x10\xf5\x03\x1a\xa3\x08\n\x13SignedBuildMetadata\x12\x19\n\x11release_directory\x18\x01 \x01(\t\x12I\n\x06status\x18\x02 \x01(\x0e\x32\x39.chromiumos.BuildReport.SignedBuildMetadata.SigningStatus\x12\r\n\x05\x62oard\x18\x03 \x01(\t\x12#\n\x04type\x18\x04 \x01(\x0e\x32\x15.chromiumos.ImageType\x12$\n\x07\x63hannel\x18\x05 \x01(\x0e\x32\x13.chromiumos.Channel\x12\x0e\n\x06keyset\x18\x06 \x01(\t\x12\x14\n\x0ckeyset_is_mp\x18\x07 \x01(\x08\x12I\n\x05\x66iles\x18\x08 \x03(\x0b\x32:.chromiumos.BuildReport.SignedBuildMetadata.FileWithHashes\x12\x45\n\x08versions\x18\t \x03(\x0b\x32\x33.chromiumos.BuildReport.SignedBuildMetadata.Version\x1a[\n\x0e\x46ileWithHashes\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0b\n\x03md5\x18\x02 \x01(\t\x12\x0c\n\x04sha1\x18\x03 \x01(\t\x12\x0e\n\x06sha256\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x03\x1a_\n\x07Version\x12\x45\n\x04kind\x18\x01 \x01(\x0e\x32\x37.chromiumos.BuildReport.SignedBuildMetadata.VersionKind\x12\r\n\x05value\x18\x02 \x01(\t\"\xe0\x01\n\x0bVersionKind\x12\x1a\n\x16VERSION_KIND_UNDEFINED\x10\x00\x12\x19\n\x15VERSION_KIND_PLATFORM\x10\x01\x12\x1a\n\x16VERSION_KIND_MILESTONE\x10\x02\x12!\n\x1dVERSION_KIND_KEY_FIRMWARE_KEY\x10\x03\x12\x1d\n\x19VERSION_KIND_KEY_FIRMWARE\x10\x04\x12\x1f\n\x1bVERSION_KIND_KEY_KERNEL_KEY\x10\x05\x12\x1b\n\x17VERSION_KIND_KEY_KERNEL\x10\x06\"\xf2\x01\n\rSigningStatus\x12\x1a\n\x16SIGNING_STATUS_UNKNOWN\x10\x00\x12\x1e\n\x1aSIGNING_STATUS_DOWNLOADING\x10\x01\x12\x1a\n\x16SIGNING_STATUS_SIGNING\x10\x02\x12\x1c\n\x18SIGNING_STATUS_UPLOADING\x10\x03\x12\x1b\n\x17SIGNING_STATUS_FINISHED\x10\x04\x12\x18\n\x14SIGNING_STATUS_RETRY\x10\x05\x12\x19\n\x15SIGNING_STATUS_PASSED\x10\x06\x12\x19\n\x15SIGNING_STATUS_FAILED\x10\x07\x1a\xca\x03\n\x07Payload\x12\x36\n\x07payload\x18\x01 \x01(\x0b\x32%.chromiumos.BuildReport.BuildArtifact\x12\x41\n\x0cpayload_type\x18\x02 \x01(\x0e\x32+.chromiumos.BuildReport.Payload.PayloadType\x12\r\n\x05\x62oard\x18\x03 \x01(\t\x12$\n\x07\x63hannel\x18\x04 \x01(\x0e\x32\x13.chromiumos.Channel\x12\r\n\x05\x61ppid\x18\x05 \x01(\t\x12\x1a\n\x12metadata_signature\x18\x06 \x01(\t\x12\x15\n\rmetadata_size\x18\x07 \x01(\x03\x12\x16\n\x0esource_version\x18\x08 \x01(\t\x12\x16\n\x0etarget_version\x18\t \x01(\t\x12\x0c\n\x04size\x18\n \x01(\x03\x12\x1c\n\x14recovery_key_version\x18\x0b \x01(\r\"q\n\x0bPayloadType\x12\x18\n\x14PAYLOAD_TYPE_UNKNOWN\x10\x00\x12\x19\n\x15PAYLOAD_TYPE_STANDARD\x10\x01\x12\x17\n\x13PAYLOAD_TYPE_MINIOS\x10\x02\x12\x14\n\x10PAYLOAD_TYPE_DLC\x10\x03\x1a\x65\n\x04\x44LCs\x12&\n\rdlc_artifacts\x18\x01 \x03(\x0b\x32\x0f.chromiumos.URI\x12\x35\n\x14\x64lc_artifact_details\x18\x02 \x03(\x0b\x32\x17.chromiumos.DlcArtifact\"\xb5\x01\n\tBuildType\x12\x18\n\x14\x42UILD_TYPE_UNDEFINED\x10\x00\x12\x16\n\x12\x42UILD_TYPE_RELEASE\x10\x01\x12\x17\n\x13\x42UILD_TYPE_FIRMWARE\x10\x02\x12\x16\n\x12\x42UILD_TYPE_FACTORY\x10\x03\x12\x15\n\x11\x42UILD_TYPE_PUBLIC\x10\x04\x12\x15\n\x11\x42UILD_TYPE_PAYGEN\x10\x05\x12\x17\n\x13\x42UILD_TYPE_SNAPSHOT\x10\x06\x42\x04\n\x02idBY\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.build_report_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos'
  _BUILDREPORT_STEPDETAILS_INFOENTRY._options = None
  _BUILDREPORT_STEPDETAILS_INFOENTRY._serialized_options = b'8\001'
  _TIMEFRAME._serialized_start=103
  _TIMEFRAME._serialized_end=198
  _BUILDID._serialized_start=200
  _BUILDID._serialized_end=241
  _URI._serialized_start=243
  _URI._serialized_end=270
  _DLCARTIFACT._serialized_start=272
  _DLCARTIFACT._serialized_end=343
  _BUILDREPORT._serialized_start=346
  _BUILDREPORT._serialized_end=5756
  _BUILDREPORT_BUILDSTATUS._serialized_start=1019
  _BUILDREPORT_BUILDSTATUS._serialized_end=1255
  _BUILDREPORT_BUILDSTATUS_STATUS._serialized_start=1094
  _BUILDREPORT_BUILDSTATUS_STATUS._serialized_end=1255
  _BUILDREPORT_BUILDCONFIG._serialized_start=1258
  _BUILDREPORT_BUILDCONFIG._serialized_end=2681
  _BUILDREPORT_BUILDCONFIG_MODEL._serialized_start=1755
  _BUILDREPORT_BUILDCONFIG_MODEL._serialized_end=2166
  _BUILDREPORT_BUILDCONFIG_MODEL_MODELVERSION._serialized_start=1877
  _BUILDREPORT_BUILDCONFIG_MODEL_MODELVERSION._serialized_end=1980
  _BUILDREPORT_BUILDCONFIG_MODEL_MODELVERSIONKIND._serialized_start=1983
  _BUILDREPORT_BUILDCONFIG_MODEL_MODELVERSIONKIND._serialized_end=2166
  _BUILDREPORT_BUILDCONFIG_RELEASE._serialized_start=2168
  _BUILDREPORT_BUILDCONFIG_RELEASE._serialized_end=2216
  _BUILDREPORT_BUILDCONFIG_BRANCH._serialized_start=2218
  _BUILDREPORT_BUILDCONFIG_BRANCH._serialized_end=2240
  _BUILDREPORT_BUILDCONFIG_VERSION._serialized_start=2242
  _BUILDREPORT_BUILDCONFIG_VERSION._serialized_end=2329
  _BUILDREPORT_BUILDCONFIG_TARGET._serialized_start=2331
  _BUILDREPORT_BUILDCONFIG_TARGET._serialized_end=2353
  _BUILDREPORT_BUILDCONFIG_VERSIONKIND._serialized_start=2356
  _BUILDREPORT_BUILDCONFIG_VERSIONKIND._serialized_end=2681
  _BUILDREPORT_BUILDARTIFACT._serialized_start=2684
  _BUILDREPORT_BUILDARTIFACT._serialized_end=3116
  _BUILDREPORT_BUILDARTIFACT_TYPE._serialized_start=2865
  _BUILDREPORT_BUILDARTIFACT_TYPE._serialized_end=3116
  _BUILDREPORT_STEPDETAILS._serialized_start=3119
  _BUILDREPORT_STEPDETAILS._serialized_end=3940
  _BUILDREPORT_STEPDETAILS_STEPINFO._serialized_start=3258
  _BUILDREPORT_STEPDETAILS_STEPINFO._serialized_end=3383
  _BUILDREPORT_STEPDETAILS_INFOENTRY._serialized_start=3385
  _BUILDREPORT_STEPDETAILS_INFOENTRY._serialized_end=3474
  _BUILDREPORT_STEPDETAILS_STATUS._serialized_start=3477
  _BUILDREPORT_STEPDETAILS_STATUS._serialized_end=3678
  _BUILDREPORT_STEPDETAILS_STEPNAME._serialized_start=3681
  _BUILDREPORT_STEPDETAILS_STEPNAME._serialized_end=3940
  _BUILDREPORT_SIGNEDBUILDMETADATA._serialized_start=3943
  _BUILDREPORT_SIGNEDBUILDMETADATA._serialized_end=5002
  _BUILDREPORT_SIGNEDBUILDMETADATA_FILEWITHHASHES._serialized_start=4342
  _BUILDREPORT_SIGNEDBUILDMETADATA_FILEWITHHASHES._serialized_end=4433
  _BUILDREPORT_SIGNEDBUILDMETADATA_VERSION._serialized_start=4435
  _BUILDREPORT_SIGNEDBUILDMETADATA_VERSION._serialized_end=4530
  _BUILDREPORT_SIGNEDBUILDMETADATA_VERSIONKIND._serialized_start=4533
  _BUILDREPORT_SIGNEDBUILDMETADATA_VERSIONKIND._serialized_end=4757
  _BUILDREPORT_SIGNEDBUILDMETADATA_SIGNINGSTATUS._serialized_start=4760
  _BUILDREPORT_SIGNEDBUILDMETADATA_SIGNINGSTATUS._serialized_end=5002
  _BUILDREPORT_PAYLOAD._serialized_start=5005
  _BUILDREPORT_PAYLOAD._serialized_end=5463
  _BUILDREPORT_PAYLOAD_PAYLOADTYPE._serialized_start=5350
  _BUILDREPORT_PAYLOAD_PAYLOADTYPE._serialized_end=5463
  _BUILDREPORT_DLCS._serialized_start=5465
  _BUILDREPORT_DLCS._serialized_end=5566
  _BUILDREPORT_BUILDTYPE._serialized_start=5569
  _BUILDREPORT_BUILDTYPE._serialized_end=5750
# @@protoc_insertion_point(module_scope)
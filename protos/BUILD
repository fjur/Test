load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_library")

py_proto_library(
    name = "payment_py_pb2",
    protos = ["payment.proto"],
    visibility = ["//visibility:public"]
)

py_proto_library(
    name = "telemetry_py_pb2",
    protos = ["telemetry.proto"],
    # visibility = ["//visibility:public"],
    visibility = ["//telemetry:__pkg__"]
)
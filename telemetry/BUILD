# py_library(
#     name = "telemetry",
#     srcs = ["telemetry_server.py"],
#     deps = [
#         "//protos:telemetry_py_pb2"
#     ]
# )

py_binary(
    name = "telemetry_server",
    main = "telemetry_server.py",
    srcs = ["telemetry_server.py"],
    deps = [
        "//protos:telemetry_py_pb2"
    ]
)

py_binary(
    name = "telemetry_client",
    main = "telemetry_client.py",
    srcs = ["telemetry_client.py"],
    deps = [
        "//protos:telemetry_py_pb2"
    ]
)
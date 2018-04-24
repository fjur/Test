# === Python Integration ===
# Use our own fork since it forces python3.
http_archive(
    name = "io_bazel_rules_python",
    strip_prefix = "rules_python-master",
    urls = ["https://github.com/vilhelm/rules_python/archive/master.zip"],
)

# === Protobuf Integration
http_archive(
    name = "org_pubref_rules_protobuf",
    strip_prefix = "rules_protobuf-master",
    urls = ["https://github.com/pubref/rules_protobuf/archive/master.zip"],
)

load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_repositories")

py_proto_repositories()
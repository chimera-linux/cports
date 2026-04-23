pkgname = "grpc"
pkgver = "1.72.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DgRPC_ABSL_PROVIDER=package",
    "-DgRPC_BENCHMARK_PROVIDER=package",
    "-DgRPC_CARES_PROVIDER=package",
    "-DgRPC_PROTOBUF_PROVIDER=package",
    "-DgRPC_RE2_PROVIDER=package",
    "-DgRPC_SSL_PROVIDER=package",
    "-DgRPC_ZLIB_PROVIDER=package",
    "-DCMAKE_CXX_STANDARD=17",
    "-DgRPC_BUILD_GRPCPP_OTEL_PLUGIN=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DgRPC_BUILD_TESTS=OFF",
    "-DgRPC_INSTALL=ON",
    "-DgRPC_DOWNLOAD_ARCHIVES=OFF",
]
make_dir = "cmake/build"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "abseil-cpp-devel",
    "benchmark-devel",
    "c-ares-devel",
    "openssl3-devel",
    "protobuf-devel",
    "re2-devel",
    "zlib-ng-compat-devel",
]
checkdepends = [
    "bash",
    "iproute2",
    "procps",
    "python-pyyaml",
    "python-six",
    "python-twisted",
]
pkgdesc = "Universal RPC framework"
license = "Apache-2.0"
url = "https://grpc.io"
source = [
    f"https://github.com/grpc/grpc/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/google/googletest/archive/4d660bf5cfb3394ac81ae57306c4964adc1b6c28.tar.gz",
    "https://github.com/envoyproxy/data-plane-api/archive/4de3c74cf21a9958c1cf26d8993c55c6e0d28b49.tar.gz",
    "https://github.com/googleapis/googleapis/archive/fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0.tar.gz",
    "https://github.com/bufbuild/protoc-gen-validate/archive/32c2415389a3538082507ae537e7edd9578c64ed.tar.gz",
    "https://github.com/cncf/xds/archive/3a472e524827f72d1ad621c4983dd5af54c46776.tar.gz",
]
source_paths = [
    ".",
    "third_party/googletest",
    "third_party/envoy-api",
    "third_party/googleapis",
    "third_party/protoc-gen-validate",
    "third_party/xds",
]
sha256 = [
    "4a8aa99d5e24f80ea6b7ec95463e16af5bd91aa805e26c661ef6491ae3d2d23c",
    "a47470a6dd5fb720cfb11c3302c87d24b857d867f6bf8a0ff082808233e0452d",
    "cd8b49614408b43bd45d90e3e98d69e24eea632ff42ac3bfb8bca68bc31e377f",
    "0513f0f40af63bd05dc789cacc334ab6cec27cc89db596557cb2dfe8919463e4",
    "a9faaabb7fcc70d1bd2b3fdd1616f3ea0cd3522e0c2a37330966536a92697ed3",
    "dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927",
]

# ring_hash_test SIGABRT
# 50323 down_cast.h:36] Check failed: dynamic_cast<To>(f) != nullptr ((null) vs. (null))
options = ["!check"]


def check(self):
    # it takes 58 mins to run
    disabled_tests = [
        "grpc_tool_test",
    ]
    regex_pattern = "|".join(disabled_tests)

    self.do(
        "python3",
        "tools/run_tests/run_tests.py",
        "-t",
        "-l",
        "c",
        "--regex_exclude",
        regex_pattern,
    )
    self.do(
        "python3",
        "tools/run_tests/run_tests.py",
        "-t",
        "-l",
        "c++",
        "--regex_exclude",
        regex_pattern,
    )


@subpackage("grpc-devel")
def _(self):
    return self.default_devel()

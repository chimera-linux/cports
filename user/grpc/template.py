pkgname = "grpc"
pkgver = "1.82.1"
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
# from MODULE.bazel for the release
source = [
    f"https://github.com/grpc/grpc/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/google/googletest/archive/v1.17.0.tar.gz",
    "https://github.com/envoyproxy/data-plane-api/archive/6ef568c.tar.gz",
    "https://github.com/googleapis/googleapis/archive/2193a2bf.tar.gz",
    "https://github.com/bufbuild/protoc-gen-validate/archive/v1.2.1.tar.gz",
    "https://github.com/cncf/xds/archive/ee656c7.tar.gz",
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
    "d74186d8fa221cc7f07ec2db970098302559f73612f6cf340cfe754848c4fc29",
    "65fab701d9829d38cb77c14acdc431d2108bfdbf8979e40eb8ae567edf10b27c",
    "ed5e6c319f8ebcdf24a9491f866a599bb9a3c193b859a94ad13bd31f85b46855",
    "3de3a199400eea7a766091aeb96c4b84c86266ad1f933f9933bbb7c359e727fe",
    "e4718352754df1393b8792b631338aa8562f390e8160783e365454bc11d96328",
    "49535f3c3370004309da50194c09bbfc528d4702424dd46e7d56a278a3dfc15d",
]
# silence noise
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
# tons of "binary not found", can't start http server in sandbox
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

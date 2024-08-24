pkgname = "grpc"
pkgver = "1.66.1"
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
    "-DBUILD_SHARED_LIBS=ON",
    # "-DgRPC_BUILD_TESTS=ON",
    "-DgRPC_INSTALL=ON",
    "-DgRPC_DOWNLOAD_ARCHIVES=OFF",
]
make_dir = "cmake/build"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "abseil-cpp-devel",
    "benchmark-devel",
    "c-ares-devel",
    "openssl-devel",
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
maintainer = "sonata-chen <sonatachen39@gmail.com>"
license = "Apache-2.0"
url = "https://grpc.io"
source = [
    f"https://github.com/grpc/grpc/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/google/googletest/archive/2dd1c131950043a8ad5ab0d2dda0e0970596586a.tar.gz",
]
source_paths = [".", "third_party/googletest"]
sha256 = [
    "79ed4ab72fa9589b20f8b0b76c16e353e4cfec1d773d33afad605d97b5682c61",
    "31bf78bd91b96dd5e24fab3bb1d7f3f7453ccbaceec9afb86d6e4816a15ab109",
]

# ring_hash_test SIGABRT
# 50323 down_cast.h:36] Check failed: dynamic_cast<To>(f) != nullptr ((null) vs. (null))
options = ["!check"]


def do_check(self):
    disabled_tests = [
        # it takes 58 mins to run
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

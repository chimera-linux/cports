pkgname = "apache-arrow"
pkgver = "20.0.0"
pkgrel = 0
_arrowsha = "d2a13712303498963395318a4eb42872e66aead7"
_parquetsha = "18d17540097fca7c40be3d42c167e6bfad90763c"
build_wrksrc = "cpp"
build_style = "cmake"
configure_args = [
    "-DARROW_BUILD_EXAMPLES=OFF",
    "-DARROW_BUILD_STATIC=OFF",
    "-DARROW_BUILD_TESTS=ON",
    "-DARROW_DEPENDENCY_SOURCE=SYSTEM",
    "-DARROW_COMPUTE=ON",
    "-DARROW_CSV=ON",
    "-DARROW_DATASET=ON",
    "-DARROW_FILESYSTEM=ON",
    "-DARROW_FLIGHT=ON",
    "-DARROW_HDFS=ON",
    "-DARROW_JSON=ON",
    "-DARROW_JSON=ON",
    "-DARROW_MIMALLOC=OFF",
    "-DARROW_ORC=OFF",
    "-DARROW_PARQUET=ON",
    "-DARROW_SIMD_LEVEL=NONE",
    "-DARROW_TENSORFLOW=ON",
    "-DARROW_USE_GLOG=ON",
    "-DARROW_USE_LLD=ON",
    "-DARROW_WITH_BROTLI=ON",
    "-DARROW_WITH_BZ2=ON",
    "-DARROW_WITH_LZ4=ON",
    "-DARROW_WITH_MUSL=ON",
    "-DARROW_WITH_SNAPPY=ON",
    "-DARROW_WITH_ZLIB=ON",
    "-DARROW_WITH_ZSTD=ON",
    "-DPARQUET_REQUIRE_ENCRYPTION=ON",
    "-DLZ4_ROOT=/usr",
]
make_check_args = [
    "-E",
    "arrow-array-test|arrow-compute-scalar-temporal-test|arrow-utility-test|arrow-csv-test|arrow-ipc-json-simple-test|arrow-dataset-file-parquet-test",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "brotli-devel",
    "glog-devel",
    "grpc-devel",
    "gtest-devel",
    "libevent-devel",
    "lz4-devel",
    "openssl3-devel",
    "protobuf-devel",
    "rapidjson",
    "re2-devel",
    "snappy-devel",
    "thrift-devel",
    "utf8proc-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Multi-language toolbox for fast data interchange and processing"
license = "Apache-2.0"
url = "https://arrow.apache.org"
source = [
    f"https://archive.apache.org/dist/arrow/arrow-{pkgver}/apache-arrow-{pkgver}.tar.gz",
    f"https://github.com/apache/arrow-testing/archive/{_arrowsha}.tar.gz",
    f"https://github.com/apache/parquet-testing/archive/{_parquetsha}.tar.gz",
]
source_paths = [
    ".",
    "cpp/arrow-testing",
    "cpp/parquet-testing",
]
sha256 = [
    "89efbbf852f5a1f79e9c99ab4c217e2eb7f991837c005cba2d4a2fbd35fad212",
    "9cca062005e329a6a60a30e28f509f5f4bd12384035b64fcaab19a5a46343cc1",
    "4496522640dc88635a8bf3c8e7572a5815549188fa00df132eef6e2a97ce0652",
]


match self.profile().arch:
    case "aarch64" | "x86_64":
        configure_args += ["-DARROW_RUNTIME_SIMD_LEVEL=MAX"]
        makedepends += ["xsimd"]
    case _:
        configure_args += ["-DARROW_RUNTIME_SIMD_LEVEL=NONE"]


def init_check(self):
    self.make_check_env["ARROW_TEST_DATA"] = str(
        self.chroot_cwd / "arrow-testing/data"
    )
    self.make_check_env["PARQUET_TEST_DATA"] = str(
        self.chroot_cwd / "parquet-testing/data"
    )


@subpackage("apache-arrow-devel")
def _(self):
    return self.default_devel()

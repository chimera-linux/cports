pkgname = "protobuf"
pkgver = "27.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-Dprotobuf_USE_EXTERNAL_GTEST=ON",
    "-Dprotobuf_ABSL_PROVIDER=package",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "gtest-devel", "abseil-cpp-devel"]
pkgdesc = "Protocol buffers library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"https://github.com/protocolbuffers/protobuf/archive/v{pkgver}.tar.gz"
sha256 = "1535151efbc7893f38b0578e83cac584f2819974f065698976989ec71c1af84a"
# FIXME vis breaks linking lite-test, cfi makes protoc not compile any tests
hardening = ["!vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protoc"]  # needs host protoc
    broken = "generated protobuf-targets.cmake looks for protoc in target sysroot, cannot cross-build android-tools etc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-lite")
def _lite(self):
    self.subdesc = "lite version"

    return ["usr/lib/libprotobuf-lite.so.*"]


@subpackage("protoc")
def _protoc(self):
    self.pkgdesc = "Protocol buffers compiler and its library"
    self.depends = [self.with_pkgver("protobuf-devel")]

    return [
        "usr/bin",
        "usr/lib/libprotoc.so.*",
    ]


@subpackage("protobuf-devel-static")
def _devel_static(self):
    return ["usr/lib/*.a"]


@subpackage("protobuf-devel")
def _devel(self):
    self.depends = [self.with_pkgver("protobuf-devel-static")]
    return self.default_devel()

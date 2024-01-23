pkgname = "protobuf"
pkgver = "25.2"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-Dprotobuf_USE_EXTERNAL_GTEST=ON",
    "-Dprotobuf_ABSL_PROVIDER=package",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel", "gtest-devel", "abseil-cpp-devel"]
pkgdesc = "Protocol buffers library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"https://github.com/protocolbuffers/protobuf/archive/v{pkgver}.tar.gz"
sha256 = "8ff511a64fc46ee792d3fe49a5a1bcad6f7dc50dfbba5a28b0e5b979c17f9871"
# FIXME vis breaks linking lite-test, cfi makes protoc not compile any tests
hardening = ["!vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protoc"]  # needs host protoc
    broken = "generated protobuf-targets.cmake looks for protoc in target sysroot, cannot cross-build android-tools etc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-lite")
def _lite(self):
    self.pkgdesc = f"{pkgdesc} (lite version)"

    return ["usr/lib/libprotobuf-lite.so.*"]


@subpackage("protoc")
def _protoc(self):
    self.pkgdesc = "Protocol buffers compiler and its library"

    return [
        "usr/bin",
        "usr/lib/libprotoc.so.*",
    ]


@subpackage("protobuf-devel")
def _devel(self):
    return self.default_devel()

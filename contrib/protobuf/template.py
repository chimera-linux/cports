pkgname = "protobuf"
pkgver = "24.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-Dprotobuf_USE_EXTERNAL_GTEST=ON",
    "-Dprotobuf_ABSL_PROVIDER=package",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel", "gtest-devel", "abseil-cpp-devel"]
pkgdesc = "Protocol buffers compiler"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"https://github.com/protocolbuffers/protobuf/archive/v{pkgver}.tar.gz"
sha256 = "616bb3536ac1fff3fb1a141450fa28b875e985712170ea7f1bfe5e5fc41e2cd8"
# FIXME cfi makes protoc not compile any tests
hardening = ["vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protobuf"]  # needs host protoc
    broken = "generated protobuf-targets.cmake looks for protoc in target sysroot, cannot cross-build android-tools etc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libprotobuf")
def _libprotobuf(self):
    self.pkgdesc = "Protocol buffers C++ library"

    return ["usr/lib/libprotobuf.so.*"]


@subpackage("libprotobuf-lite")
def _libprotobuf_lite(self):
    self.pkgdesc = "Protocol buffers C++ library (lite version)"

    return ["usr/lib/libprotobuf-lite.so.*"]


@subpackage("libprotoc")
def _libprotoc(self):
    self.pkgdesc = "Protocol buffers compiler library"

    return ["usr/lib/libprotoc.so.*"]


@subpackage("protobuf-devel")
def _devel(self):
    return self.default_devel()

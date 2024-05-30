pkgname = "protobuf"
pkgver = "27.1"
pkgrel = 0
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
sha256 = "6fbe2e6f703bcd3a246529c2cab586ca12a98c4e641f5f71d51fde09eb48e9e7"
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
    self.depends = [f"protobuf-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/bin",
        "usr/lib/libprotoc.so.*",
    ]


@subpackage("protobuf-devel-static")
def _devel_static(self):
    self.pkgdesc = f"{pkgdesc} (development files) (static libraries)"
    return ["usr/lib/*.a"]


@subpackage("protobuf-devel")
def _devel(self):
    self.depends = [f"protobuf-devel-static={pkgver}-r{pkgrel}"]
    return self.default_devel()

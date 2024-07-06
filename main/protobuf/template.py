pkgname = "protobuf"
pkgver = "27.2"
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
sha256 = "e4ff2aeb767da6f4f52485c2e72468960ddfe5262483879ef6ad552e52757a77"
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

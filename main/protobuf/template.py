pkgname = "protobuf"
pkgver = "29.1"
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
sha256 = "3d32940e975c4ad9b8ba69640e78f5527075bae33ca2890275bf26b853c0962c"
# FIXME vis breaks linking lite-test, cfi makes protoc not compile any tests
hardening = ["!vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protoc"]  # needs host protoc
    broken = "generated protobuf-targets.cmake looks for protoc in target sysroot, cannot cross-build android-tools etc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-utf8range")
def _(self):
    self.subdesc = "internal utf8range library"

    return ["usr/lib/libutf8_*"]


@subpackage("protobuf-lite")
def _(self):
    self.subdesc = "lite version"

    return ["usr/lib/libprotobuf-lite.so.*"]


@subpackage("protoc")
def _(self):
    self.pkgdesc = "Protocol buffers compiler and its library"
    self.depends = [self.with_pkgver("protobuf-devel")]

    return [
        "usr/bin",
        "usr/lib/libprotoc.so.*",
    ]


@subpackage("protobuf-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("protobuf-devel")
def _(self):
    self.depends = [self.with_pkgver("protobuf-devel-static")]
    return self.default_devel()

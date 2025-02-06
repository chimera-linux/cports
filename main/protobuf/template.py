pkgname = "protobuf"
pkgver = "29.3"
pkgrel = 2
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
sha256 = "008a11cc56f9b96679b4c285fd05f46d317d685be3ab524b2a310be0fbad987e"
# FIXME vis breaks linking lite-test, cfi makes protoc not compile any tests
hardening = ["!vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protobuf-protoc"]  # needs host protoc
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


@subpackage("protobuf-protoc")
def _(self):
    self.pkgdesc = "Protocol buffers compiler and its library"
    self.depends = [self.with_pkgver("protobuf-devel")]
    self.provides = [self.with_pkgver("protoc")]

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

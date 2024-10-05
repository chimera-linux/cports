pkgname = "libdeflate"
pkgver = "1.22"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBDEFLATE_BUILD_STATIC_LIB=OFF",
    "-DLIBDEFLATE_BUILD_TESTS=ON",
    "-DLIBDEFLATE_USE_SHARED_LIB=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for DEFLATE/zlib/gzip compression and decompression"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ebiggers/libdeflate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7f343c7bf2ba46e774d8a632bf073235e1fd27723ef0a12a90f8947b7fe851d6"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdeflate-devel")
def _(self):
    return self.default_devel()


@subpackage("libdeflate-progs")
def _(self):
    return self.default_progs()

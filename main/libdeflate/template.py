pkgname = "libdeflate"
pkgver = "1.20"
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
sha256 = "ed1454166ced78913ff3809870a4005b7170a6fd30767dc478a09b96847b9c2a"
# FIXME: cfi
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdeflate-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libdeflate-progs")
def _progs(self):
    return self.default_progs()

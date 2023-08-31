pkgname = "libdeflate"
pkgver = "1.18"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBDEFLATE_BUILD_TESTS=ON",
    "-DLIBDEFLATE_USE_SHARED_LIB=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "zlib-devel",
]
pkgdesc = "Library for DEFLATE/zlib/gzip compression and decompression"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ebiggers/libdeflate"
source = (
    f"https://github.com/ebiggers/libdeflate/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "225d982bcaf553221c76726358d2ea139bb34913180b20823c782cede060affd"
# FIXME: cfi
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    # for some reason the link points to a full destdir path (and is also hard by default)
    self.rm(self.destdir / "usr/bin/libdeflate-gunzip")
    self.install_link("libdeflate-gzip", "usr/bin/libdeflate-gunzip")


@subpackage("libdeflate-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libdeflate-progs")
def _progs(self):
    return self.default_progs()

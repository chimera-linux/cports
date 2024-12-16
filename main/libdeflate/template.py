pkgname = "libdeflate"
pkgver = "1.23"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ebiggers/libdeflate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1ab18349b9fb0ce8a0ca4116bded725be7dcbfa709e19f6f983d99df1fb8b25f"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdeflate-devel")
def _(self):
    return self.default_devel()


@subpackage("libdeflate-progs")
def _(self):
    return self.default_progs()

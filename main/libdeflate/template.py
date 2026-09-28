pkgname = "libdeflate"
pkgver = "1.25"
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
license = "MIT"
url = "https://github.com/ebiggers/libdeflate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d11473c1ad4c57d874695e8026865e38b47116bbcb872bfc622ec8f37a86017d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdeflate-devel")
def _(self):
    return self.default_devel()


@subpackage("libdeflate-progs")
def _(self):
    return self.default_progs()

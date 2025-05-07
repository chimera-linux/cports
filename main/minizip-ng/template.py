pkgname = "minizip-ng"
pkgver = "4.0.10"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DMZ_LIB_SUFFIX=-ng"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "bzip2-devel",
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-devel",
    "zstd-devel",
]
pkgdesc = "Fork of the popular zip manipulation library"
license = "Zlib"
url = "https://github.com/zlib-ng/minizip-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c362e35ee973fa7be58cc5e38a4a6c23cc8f7e652555daf4f115a9eb2d3a6be7"


@subpackage("minizip-ng-devel")
def _(self):
    return self.default_devel()

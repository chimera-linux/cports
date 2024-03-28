pkgname = "minizip-ng"
pkgver = "4.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DMZ_LIB_SUFFIX=-ng"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "bzip2-devel",
    "openssl-devel",
    "xz-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Fork of the popular zip manipulation library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/zlib-ng/minizip-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9bb636474b8a4269280d32aca7de4501f5c24cc642c9b4225b4ed7b327f4ee73"


@subpackage("minizip-ng-devel")
def _devel(self):
    return self.default_devel()

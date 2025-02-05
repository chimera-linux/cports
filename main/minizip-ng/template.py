pkgname = "minizip-ng"
pkgver = "4.0.8"
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/zlib-ng/minizip-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c3e9ceab2bec26cb72eba1cf46d0e2c7cad5d2fe3adf5df77e17d6bbfea4ec8f"


@subpackage("minizip-ng-devel")
def _(self):
    return self.default_devel()

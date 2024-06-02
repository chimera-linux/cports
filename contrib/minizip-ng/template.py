pkgname = "minizip-ng"
pkgver = "4.0.6"
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
sha256 = "e96ed3866706a67dbed05bf035e26ef6b60f408e1381bf0fe9af17fe2c0abebc"


@subpackage("minizip-ng-devel")
def _devel(self):
    return self.default_devel()

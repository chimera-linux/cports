pkgname = "minizip-ng"
pkgver = "4.0.7"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DMZ_LIB_SUFFIX=-ng"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "bzip2-devel",
    "openssl-devel",
    "xz-devel",
    "zlib-ng-devel",
    "zstd-devel",
]
pkgdesc = "Fork of the popular zip manipulation library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/zlib-ng/minizip-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a87f1f734f97095fe1ef0018217c149d53d0f78438bcb77af38adc21dff2dfbc"


@subpackage("minizip-ng-devel")
def _(self):
    return self.default_devel()

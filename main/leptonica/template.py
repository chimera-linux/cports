pkgname = "leptonica"
pkgver = "1.85.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "giflib-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Image processing library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause"
url = "http://www.leptonica.org"
source = f"https://github.com/DanBloomberg/leptonica/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c01376bce0379d4ea4bc2ec5d5cbddaa49e2f06f88242619ab8c059e21adf233"


def post_install(self):
    self.install_license("leptonica-license.txt")


@subpackage("leptonica-devel")
def _(self):
    return self.default_devel()

pkgname = "leptonica"
pkgver = "1.84.1"
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
sha256 = "ecd7a868403b3963c4e33623595d77f2c87667e2cfdd9b370f87729192061bef"


def post_install(self):
    self.install_license("leptonica-license.txt")


@subpackage("leptonica-devel")
def _(self):
    return self.default_devel()

pkgname = "raqm"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "freetype-devel",
    "fribidi-devel",
    "harfbuzz-devel",
]
pkgdesc = "Library for complex text layout"
license = "MIT"
url = "https://host-oman.github.io/libraqm"
source = f"https://github.com/HOST-Oman/libraqm/releases/download/v{pkgver}/raqm-{pkgver}.tar.xz"
sha256 = "3d0add115f7d4a9410d3377462ed3c05e86342193ef984183e4380e3787b2d4c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("raqm-devel")
def _(self):
    return self.default_devel()

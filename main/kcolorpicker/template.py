pkgname = "kcolorpicker"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_EXAMPLE=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTS=ON",
    "-DBUILD_WITH_QT6=ON",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Qt based color picker"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/ksnip/kColorPicker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e78c785ec4a8a22a48a91835c97601f5704b5076b154415353b0d2697dc0b4f7"
hardening = ["vis", "cfi"]


@subpackage("kcolorpicker-devel")
def _(self):
    return self.default_devel()

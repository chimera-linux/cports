pkgname = "xcb-imdkit"
pkgver = "1.0.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "xcb-util-devel",
    "xcb-util-keysyms-devel",
    "uthash-devel",
]
pkgdesc = "X input method support for XCB"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-only"
url = "https://github.com/fcitx/xcb-imdkit"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c904dae07f9c971b21ef43b7ae9a2018a1b3ceda0ea5c44efbdb61a7c8b161f8"


@subpackage("xcb-imdkit-devel")
def _devel(self):
    return self.default_devel()

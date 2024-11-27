pkgname = "xcb-imdkit"
pkgver = "1.0.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "uthash",
    "xcb-util-devel",
    "xcb-util-keysyms-devel",
]
pkgdesc = "X input method support for XCB"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/fcitx/xcb-imdkit"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c2f0bbad8a335a64cdc7c19ac7b6ea1f0887dd6300ca9a4fa2e2fec6b9d3f695"
hardening = ["vis", "!cfi"]


@subpackage("xcb-imdkit-devel")
def _(self):
    return self.default_devel()

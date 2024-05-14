pkgname = "xcb-imdkit"
pkgver = "1.0.8"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only"
url = "https://github.com/fcitx/xcb-imdkit"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bea897d27df2b66bbff144ba85a1e183dbc1a6a5bd6179abed11aef21ab2e38a"
# FIXME: cfi
hardening = ["vis"]


@subpackage("xcb-imdkit-devel")
def _devel(self):
    return self.default_devel()

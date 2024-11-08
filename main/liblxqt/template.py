pkgname = "liblxqt"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "libqtxdg-devel",
    "libxscrnsaver-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Core utility library for all LXQt components"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/liblxqt"
source = f"{url}/releases/download/{pkgver}/liblxqt-{pkgver}.tar.xz"
sha256 = "10820b62f83c5f53439b8690c9d71deaad7aa31e6506f9ec53cb789d47b13ce0"


@subpackage("liblxqt-devel")
def _(self):
    return self.default_devel()

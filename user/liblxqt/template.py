pkgname = "liblxqt"
pkgver = "2.5.1"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/liblxqt"
source = f"{url}/releases/download/{pkgver}/liblxqt-{pkgver}.tar.xz"
sha256 = "5afcd6093733434e8c91d4fea583fc3597f35f1b751eed750e5e31e1beed063d"


@split("devel")
def _(self):
    return self.default_devel()

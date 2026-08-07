pkgname = "liblxqt"
pkgver = "2.4.0"
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
sha256 = "6627215644eb370723536274555743db52baed919db6ffc32ebc2bdf3cf8ee4a"


@subpackage("liblxqt-devel")
def _(self):
    return self.default_devel()

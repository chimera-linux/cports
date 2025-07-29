pkgname = "liblxqt"
pkgver = "2.2.0"
pkgrel = 1
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
sha256 = "4a898b1bf059fb73102011bca79bb96d33c49c95f6d56135ef13a8e91d0a09c8"


@subpackage("liblxqt-devel")
def _(self):
    return self.default_devel()

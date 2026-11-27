pkgname = "qtermwidget"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "pkgconf"]
makedepends = ["qt6-qtbase-devel", "qt6-qttools-devel"]
pkgdesc = "Terminal widget for QTerminal"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/qtermwidget"
source = f"{url}/releases/download/{pkgver}/qtermwidget-{pkgver}.tar.xz"
sha256 = "4d29fec9c3d1974278bf64f2daf8e879b3696a29d2cc35f23894340be64c51ff"


@split("devel")
def _(self):
    return self.default_devel()

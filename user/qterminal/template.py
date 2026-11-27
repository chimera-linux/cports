pkgname = "qterminal"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "layer-shell-qt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "qtermwidget-devel",
]
pkgdesc = "Lightweight Qt-based terminal emulator"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/qterminal"
source = f"{url}/releases/download/{pkgver}/qterminal-{pkgver}.tar.xz"
sha256 = "19e6ce82b4b99b92d412f3d8fcf3bff93f776e1886b6701b85707e4d2bd2e329"

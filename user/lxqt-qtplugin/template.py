pkgname = "lxqt-qtplugin"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja"]
makedepends = [
    "libdbusmenu-lxqt-devel",
    "libfm-qt-devel",
    "libqtxdg-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
]
pkgdesc = "LXQt Qt platform integration plugin"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-qtplugin"
source = f"{url}/releases/download/{pkgver}/lxqt-qtplugin-{pkgver}.tar.xz"
sha256 = "451b891d5adb946bd785e34f785dff3efc0487f92effb927f9294efee1704d22"

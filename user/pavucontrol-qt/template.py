pkgname = "pavucontrol-qt"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt Pulseaudio mixer"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/pavucontrol-qt"
source = f"{url}/releases/download/{pkgver}/pavucontrol-qt-{pkgver}.tar.xz"
sha256 = "7f813d3029e9f1b66020cf3da143d07196dd8bce01a95bd754489287ca5b6380"

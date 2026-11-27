pkgname = "pavucontrol-qt"
pkgver = "2.5.1"
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
sha256 = "a4c3839571f3d1bb556fe10c8f53316d6cc6374a98af49b1506a6aca2c5b7316"

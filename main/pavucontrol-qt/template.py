pkgname = "pavucontrol-qt"
pkgver = "2.2.0"
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
sha256 = "f1d213426ac1033d23a8239732dc7f5fdeb393b064f11c9582e01b0c8310aee9"

pkgname = "pavucontrol-qt"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "lxqt-build-tools",
    "perl",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt Pulseaudio mixer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/pavucontrol-qt"
source = f"{url}/releases/download/{pkgver}/pavucontrol-qt-{pkgver}.tar.xz"
sha256 = "6c3cfc8a4bc0b232b66516b16c32ebcd2d1d1ddb144d9e3adeea6cdffb386bbf"

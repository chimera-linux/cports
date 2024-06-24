pkgname = "pavucontrol-qt"
pkgver = "2.0.0"
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
sha256 = "3acec36371614a2bb8145228449e684cea83aab31234c960176688d88e830475"

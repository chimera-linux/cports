pkgname = "pcmanfm-qt"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "layer-shell-qt-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "File manager and desktop icon manager"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/pcmanfm-qt"
source = f"{url}/releases/download/{pkgver}/pcmanfm-qt-{pkgver}.tar.xz"
sha256 = "b70d65e83f14aac2b58ebc8dd7653061c6a58083869e0b1a2d43dd7f65464c9d"
options = ["etcfiles"]

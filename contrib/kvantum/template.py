pkgname = "kvantum"
pkgver = "1.1.1"
pkgrel = 0
build_style = "cmake"
cmake_dir = "Kvantum"
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "kwindowsystem-devel",
    "libx11-devel",
    "libxext-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "SVG-based theme engine for Qt"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/tsujan/Kvantum"
source = f"{url}/releases/download/V{pkgver}/Kvantum-{pkgver}.tar.xz"
sha256 = "0ce7dc080ea36caea835bccd0f7637e19568e0b3658ccb855bc3a61faf23cda7"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

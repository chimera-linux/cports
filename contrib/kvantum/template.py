pkgname = "kvantum"
pkgver = "1.0.10"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_VERSION_MAJOR=6"]
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
sha256 = "4a070a1a6fac3d1861010aa44d34e665e4697bc64c4c5015a6448203c31f1f1f"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

cmake_dir = "Kvantum"

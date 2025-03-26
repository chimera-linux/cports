pkgname = "kvantum"
pkgver = "1.1.4"
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
license = "GPL-3.0-or-later"
url = "https://github.com/tsujan/Kvantum"
source = f"{url}/releases/download/V{pkgver}/Kvantum-{pkgver}.tar.xz"
sha256 = "0b47a7081b943a035f8cff66767d00cb134f179f5e24d6ac8362c1f2e4ca2d1b"
hardening = ["vis", "cfi", "!int"]

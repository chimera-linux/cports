pkgname = "kvantum"
pkgver = "1.1.2"
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
sha256 = "6d3ce7f535d7d08ffe59b04dd3f04a8ab83fe35024fe34cf56995b94f40d12a2"
hardening = ["vis", "cfi"]

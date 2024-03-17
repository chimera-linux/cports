pkgname = "kvantum"
pkgver = "1.1.0"
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
sha256 = "bfc5d97630c87e5b21ccab86efbc3511105c61829a75798923ec2274b7d5cd32"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

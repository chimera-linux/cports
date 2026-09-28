pkgname = "kvantum"
pkgver = "1.1.7"
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
sha256 = "0f6e8846ba3f9e2f2e41f833c54b2b0e440b81ff9ffc15221690fafef77f4b58"
hardening = ["vis", "cfi", "!int"]

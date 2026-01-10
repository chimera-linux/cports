pkgname = "featherpad"
pkgver = "1.6.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hunspell-devel",
    "libx11-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt Plain-Text editor"
license = "GPL-3.0-or-later"
url = "https://github.com/tsujan/FeatherPad"
source = f"{url}/releases/download/V{pkgver}/FeatherPad-{pkgver}.tar.xz"
sha256 = "f20a2e1b82524d181c97bb23d1b643ae374b9257a8c2c95bcaf0d0c940a2c9ee"

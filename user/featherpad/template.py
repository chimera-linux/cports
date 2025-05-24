pkgname = "featherpad"
pkgver = "1.6.2"
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
sha256 = "0c6ad7687d933e48f5e64047dacb4d4611155210ef1557874fb708e805a50daa"

pkgname = "featherpad"
pkgver = "1.6.4"
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
sha256 = "369c39059ff8978e8ce3b8575601e8ac805595cbabf1704601e829b3a745ca8a"

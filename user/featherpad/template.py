pkgname = "featherpad"
pkgver = "1.6.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/tsujan/FeatherPad"
source = f"{url}/releases/download/V{pkgver}/FeatherPad-{pkgver}.tar.xz"
sha256 = "246e7d72572a8f44a3e22bb1a9eba5672ff0e997053e19ba78abcfab5d5ca41d"

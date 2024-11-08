pkgname = "featherpad"
pkgver = "1.5.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/tsujan/FeatherPad"
source = f"{url}/releases/download/V{pkgver}/FeatherPad-{pkgver}.tar.xz"
sha256 = "d63d977c875ee18be1ef007b8cd653ae495018184ea641e2bbc812781b926e87"

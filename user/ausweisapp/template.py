pkgname = "ausweisapp"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "doxygen",
    "ninja",
    "pkgconf",
]
makedepends = [
    "pcsc-lite-devel",
    "qt6-qtbase-devel",
    "qt6-qtscxml-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebsockets-devel",
]
pkgdesc = "Official eID-Client of Germany"
license = "EUPL-1.2"
url = "https://www.ausweisapp.bund.de"
source = f"https://github.com/Governikus/AusweisApp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7508057057f37f08c385827e013253e518907b08dda96c1892a7f812306af3cc"

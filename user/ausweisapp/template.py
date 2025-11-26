pkgname = "ausweisapp"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
# Enum in qmltypes is not scoped
make_check_args = ["-E", "qmltypes"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
makedepends = [
    "openssl3-devel",
    "pcsc-lite-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtscxml-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebsockets-devel",
]
pkgdesc = "Authentication app for German ID cards"
license = "EUPL-1.2"
url = "https://www.ausweisapp.bund.de"
source = f"https://github.com/Governikus/AusweisApp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "411ef84496728239ff1e1e9bb79b8d9273ba5c15f8c0bcb12fa57d7ea2d9f787"

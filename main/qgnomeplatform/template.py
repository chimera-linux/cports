pkgname = "qgnomeplatform"
pkgver = "0.9.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUSE_QT6=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "adwaita-qt-devel",
    "gsettings-desktop-schemas",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "QPlatformTheme to integrate Qt apps into GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/FedoraQt/QGnomePlatform"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9446c0d68faccdd0e44039b2089ab4524939a47cfe8c34e50b0368c2b58a5552"

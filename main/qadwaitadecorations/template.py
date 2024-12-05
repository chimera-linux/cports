pkgname = "qadwaitadecorations"
pkgver = "0.1.5"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DUSE_QT6=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qwaylanddecorationplugin_p.h etc
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "Qt decoration plugin for Adwaita decorations"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/FedoraQt/QAdwaitaDecorations"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9e3bde8332da156744f86ad09f9e0456dd63f6fcfdc330b4667f4fdc4faf7a6b"

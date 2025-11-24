pkgname = "qadwaitadecorations"
pkgver = "0.1.7"
pkgrel = 2
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
license = "LGPL-2.1-or-later"
url = "https://github.com/FedoraQt/QAdwaitaDecorations"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6cd96efca241a4b60fb6bf449c64dbad713b223c36e003ae89f45e34739d56d1"

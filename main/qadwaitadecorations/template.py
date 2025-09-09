pkgname = "qadwaitadecorations"
pkgver = "0.1.6"
pkgrel = 4
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
sha256 = "dc413ddd27ea8f5bbbfd9640f5f2c25827c035d280dc271dd8dc18c88de905e1"

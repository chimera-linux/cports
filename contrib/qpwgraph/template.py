pkgname = "qpwgraph"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "pipewire-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Pipewire graph manager"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/rncbc/qpwgraph"
source = f"{url}/-/archive/v{pkgver}/qpwgraph-v{pkgver}.tar.bz2"
sha256 = "1988716b31398ab87b11298b2d17268b8e88af00abf4c30ba7ae56844987efbb"
# FIXME: cfi
hardening = ["vis"]

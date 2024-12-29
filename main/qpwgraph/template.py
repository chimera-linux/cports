pkgname = "qpwgraph"
pkgver = "0.8.1"
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
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/rncbc/qpwgraph"
source = f"{url}/-/archive/v{pkgver}/qpwgraph-v{pkgver}.tar.gz"
sha256 = "fdfeb9e087e437ae6d10f02d31bfddd7d5acb7fc7255f167baee8808d99d38f8"

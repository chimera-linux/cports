pkgname = "qpwgraph"
pkgver = "0.6.0"
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
source = f"https://gitlab.freedesktop.org/rncbc/qpwgraph/-/archive/v{pkgver}/qpwgraph-v{pkgver}.tar.bz2"
sha256 = "899fd4fef9994c3ef8948f10b11ff185867efc394d455c0a0c3970feeca7fca3"
# FIXME: cfi
hardening = ["vis"]

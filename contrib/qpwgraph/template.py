pkgname = "qpwgraph"
pkgver = "0.5.3"
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
sha256 = "c402ac557f3ab262b2c639708157de838919e067f2f2a16c69928ad2a9e365c6"
# FIXME: cfi
hardening = ["vis"]

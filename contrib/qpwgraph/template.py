pkgname = "qpwgraph"
pkgver = "0.7.2"
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
sha256 = "a2c142ace37762425e39450ef05b1f49e1d6850a6c349fef213dc0c91e409629"
# FIXME: cfi
hardening = ["vis"]

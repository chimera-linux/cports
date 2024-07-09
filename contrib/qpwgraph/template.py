pkgname = "qpwgraph"
pkgver = "0.7.4"
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
sha256 = "46416346ef9a77faa2122ea8b7112cf4f0daf9c68454bb5a8ac2418aa25895fc"
hardening = ["vis", "!cfi"]

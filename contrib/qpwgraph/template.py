pkgname = "qpwgraph"
pkgver = "0.6.2"
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
sha256 = "562038e231e448e4c89bf9b47277ffd3e9b32f09ee818be8b7c4087cf7804698"
# FIXME: cfi
hardening = ["vis"]

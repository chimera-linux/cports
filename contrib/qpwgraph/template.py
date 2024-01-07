pkgname = "qpwgraph"
pkgver = "0.6.1"
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
sha256 = "1d701b336da4a8b7ccfe7d9a8148c1f07291284ac319cf6a85becc83d265a9cf"
# FIXME: cfi
hardening = ["vis"]

pkgname = "qpwgraph"
pkgver = "0.6.3"
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
sha256 = "d69052c77303f56ae326c2f19924efc3fde6e06ef997e937be42b29bc404398f"
# FIXME: cfi
hardening = ["vis"]

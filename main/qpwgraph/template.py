pkgname = "qpwgraph"
pkgver = "0.8.2"
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
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/rncbc/qpwgraph"
source = f"{url}/-/archive/v{pkgver}/qpwgraph-v{pkgver}.tar.gz"
sha256 = "a4e87d48f701235789c232c793de699e0ca6837af15775461dcc9a202ca2a95b"

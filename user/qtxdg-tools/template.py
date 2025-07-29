pkgname = "qtxdg-tools"
pkgver = "4.2.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libqtxdg-devel",
]
pkgdesc = "User tools for libqtxdg"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/qtxdg-tools"
source = f"{url}/releases/download/{pkgver}/qtxdg-tools-{pkgver}.tar.xz"
sha256 = "503a6e37792709340dddd642821eca13ef8d789cd26a06983cb7c5e06b8d63af"

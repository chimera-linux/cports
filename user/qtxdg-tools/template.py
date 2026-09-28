pkgname = "qtxdg-tools"
pkgver = "4.4.0"
pkgrel = 0
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
sha256 = "f21ba4308eac0effd417d910cc4916df7b6202aaeee777b51bb120f7abc6c5ac"

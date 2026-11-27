pkgname = "qtxdg-tools"
pkgver = "4.5.0"
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
sha256 = "4532035802a8b08d5475ed8b054e417366327e85f43dd3c1bf1ab1864e422701"

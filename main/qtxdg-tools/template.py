pkgname = "qtxdg-tools"
pkgver = "4.0.0"
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
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/qtxdg-tools"
source = f"{url}/releases/download/{pkgver}/qtxdg-tools-{pkgver}.tar.xz"
sha256 = "4cd485e2780290d99d7242f605db9f0ffe5ed598cc672ed5e4acef871ce27b3a"

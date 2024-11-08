pkgname = "qtxdg-tools"
pkgver = "4.1.0"
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
sha256 = "dbd59b7641091a226fb58222e11b4aeb36e6e65dc235280897d066e59fa966b6"

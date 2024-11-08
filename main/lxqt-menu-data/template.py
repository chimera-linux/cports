pkgname = "lxqt-menu-data"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "qt6-qttools-devel",
]
pkgdesc = "Menu files for LXQt components"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-menu-data"
source = f"{url}/releases/download/{pkgver}/lxqt-menu-data-{pkgver}.tar.xz"
sha256 = "d2d2187313c16fc435a7313e53b80ace7ccba0b5de6c0d9cd53bfdfa13d5eab4"

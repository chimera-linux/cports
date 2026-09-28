pkgname = "lxqt-menu-data"
pkgver = "2.4.0"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-menu-data"
source = f"{url}/releases/download/{pkgver}/lxqt-menu-data-{pkgver}.tar.xz"
sha256 = "3487e47562dc19e63358a50c81e51cd0cf1a020397943cadd8db35daeb4866cc"
options = ["etcfiles"]

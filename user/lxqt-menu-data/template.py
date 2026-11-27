pkgname = "lxqt-menu-data"
pkgver = "2.5.0"
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
sha256 = "74983c6d27d9b79ba5a20db645a554ea8065cc7e9faa657363a77988a7228a74"
options = ["etcfiles"]

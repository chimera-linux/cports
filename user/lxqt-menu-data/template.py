pkgname = "lxqt-menu-data"
pkgver = "2.2.0"
pkgrel = 1
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
sha256 = "a5a026fe3a8d279551233fa399b37139a668c70b07b53ec85c23e67249ae895b"

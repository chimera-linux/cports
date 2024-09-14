pkgname = "lxqt-menu-data"
pkgver = "2.0.0"
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
sha256 = "44768dd5dcc7c66fadd919ddd8528e22dd7ee587ef198b02dffbf05e0c0d1a52"

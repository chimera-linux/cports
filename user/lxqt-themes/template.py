pkgname = "lxqt-themes"
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
pkgdesc = "Themes, graphics and icons for LXQt"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-themes"
source = f"{url}/releases/download/{pkgver}/lxqt-themes-{pkgver}.tar.xz"
sha256 = "b39475e0fdaf5b94747141da28319694d45d4646b3d83c45917f5a1d9af432fb"

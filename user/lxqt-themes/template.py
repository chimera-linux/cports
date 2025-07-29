pkgname = "lxqt-themes"
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
pkgdesc = "Themes, graphics and icons for LXQt"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-themes"
source = f"{url}/releases/download/{pkgver}/lxqt-themes-{pkgver}.tar.xz"
sha256 = "92c5a8d8ad08ca5510a32cd82fba231606a56c9338ef633a0a98a97b02baf4f2"

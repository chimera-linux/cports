pkgname = "lxqt-themes"
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
pkgdesc = "Themes, graphics and icons for LXQt"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-themes"
source = f"{url}/releases/download/{pkgver}/lxqt-themes-{pkgver}.tar.xz"
sha256 = "35217f4b4cdcea8e7804e6f52d948587a3079eed94015992b6dea0f98dca1194"

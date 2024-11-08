pkgname = "lxqt-themes"
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
pkgdesc = "Themes, graphics and icons for LXQt"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-themes"
source = f"{url}/releases/download/{pkgver}/lxqt-themes-{pkgver}.tar.xz"
sha256 = "cdd0101c5a53a0e49315c7af3ba784e70a8a2410526eab3d63f32a6678bd0fac"

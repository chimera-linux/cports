pkgname = "lxqt-themes"
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
pkgdesc = "Themes, graphics and icons for LXQt"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-themes"
source = f"{url}/releases/download/{pkgver}/lxqt-themes-{pkgver}.tar.xz"
sha256 = "927aa0bd8ecf718c4a91e820277af12a24d329b99e9e7ca4868311c1de76911d"

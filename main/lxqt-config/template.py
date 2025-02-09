pkgname = "lxqt-config"
pkgver = "2.1.1"
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
    "kwindowsystem-devel",
    "libkscreen-devel",
    "liblxqt-devel",
    "lxqt-menu-data",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "xserver-xorg-input-libinput-devel",
]
depends = [
    "lxqt-menu-data",
]
pkgdesc = "Tools to configure LXQt and the underlying operating system"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-config"
source = f"{url}/releases/download/{pkgver}/lxqt-config-{pkgver}.tar.xz"
sha256 = "222144caa133a91c2ed7503d2988573cd3a0b09e61caa1cb45bd8a099538df3f"

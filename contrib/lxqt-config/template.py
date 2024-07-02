pkgname = "lxqt-config"
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
sha256 = "091d4a1e177f732f6d6e9e66b2e117e0272272eaa73595290ad2ea05f0c4ac73"

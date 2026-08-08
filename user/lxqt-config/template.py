pkgname = "lxqt-config"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-config"
source = f"{url}/releases/download/{pkgver}/lxqt-config-{pkgver}.tar.xz"
sha256 = "8943a0d61993e068fa71aac85eb1eb93ac32064928ee1c8c1ff9666b45e1610e"

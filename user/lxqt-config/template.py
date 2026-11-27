pkgname = "lxqt-config"
pkgver = "2.5.1"
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
sha256 = "e46d6ec711a928ba1dc202bc5eac58c025decf84fe85ff01a4b2128e17e88917"

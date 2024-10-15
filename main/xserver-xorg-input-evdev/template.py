pkgname = "xserver-xorg-input-evdev"
pkgver = "2.11.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = [
    "libevdev-devel",
    "mtdev-devel",
    "udev-devel",
    "xserver-xorg-devel",
]
depends = [
    "virtual:xserver-abi-input~24!xserver-xorg-core",
]
pkgdesc = "Generic input driver for X.org server based on evdev"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-input-evdev-{pkgver}.tar.gz"
sha256 = "6bf1d288f15f5c7db87e8ad62a75ef372789897be11d8a9706c4408b863a2add"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xorg-input-evdev-devel")
def _(self):
    return self.default_devel()

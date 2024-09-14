pkgname = "xserver-xorg-input-evdev"
pkgver = "2.10.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
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
sha256 = "502e5d196ec09f858d94caf7bf4cebaf1aa6fd37f2f87d89f4ca723746438eea"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xorg-input-evdev-devel")
def _(self):
    return self.default_devel()

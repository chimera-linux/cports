pkgname = "xserver-xorg-input-wacom"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = [
    "libx11-devel",
    "libxext-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "linux-headers",
    "udev-devel",
    "xserver-xorg-devel",
]
depends = ["virtual:xserver-abi-input~24!xserver-xorg-core"]
pkgdesc = "X.org Wacom tablet input driver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xorg.freedesktop.org"
source = f"https://github.com/linuxwacom/xf86-input-wacom/releases/download/xf86-input-wacom-{pkgver}/xf86-input-wacom-{pkgver}.tar.bz2"
sha256 = "70365826c3ca58cc81d98fab8f048f2c375e78c786111eb8a72a67a5721cb146"


def post_install(self):
    self.uninstall("usr/lib/systemd/system")


@subpackage("xserver-xorg-input-wacom-devel")
def _(self):
    return self.default_devel()

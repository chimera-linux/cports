pkgname = "xserver-xorg-input-wacom"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
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
sha256 = "70771033543097e6c616a39ae8bb40fd0e991a25560ed10c65b33756c3061511"


def post_install(self):
    self.uninstall("usr/lib/systemd/system")


@subpackage("xserver-xorg-input-wacom-devel")
def _devel(self):
    return self.default_devel()

pkgname = "xserver-xorg-input-libinput"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xserver-xorg-devel", "libinput-devel"]
depends = ["virtual:xserver-abi-input~24!xserver-xorg-core"]
pkgdesc = "Generic input driver for X.org server based on libinput"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-input-libinput-{pkgver}.tar.gz"
sha256 = "3b4f519b6b3cea852e8c008fb3a3f9f5da8b7e204c31c18d4a6d1e5875ac77f1"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xserver-xorg-input-libinput-devel")
def _devel(self):
    return self.default_devel()

pkgname = "xserver-xorg-input-libinput"
pkgver = "1.2.1"
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
sha256 = "ac37b3fd4685025d8a1864ee361b3d6c4e50689c9a5b86786ea1fa3eb997f3e5"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("xserver-xorg-input-libinput-devel")
def _devel(self):
    return self.default_devel()

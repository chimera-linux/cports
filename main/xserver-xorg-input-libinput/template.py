pkgname = "xserver-xorg-input-libinput"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xserver-xorg-devel", "libinput-devel"]
depends = ["virtual:xserver-abi-input>=24.4"]
depends_providers = {
    "virtual:xserver-abi-input": "xserver-xorg-core"
}
pkgdesc = "Generic input driver for X.org server based on libinput"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-input-libinput-{pkgver}.tar.bz2"
sha256 = "f80da3c514fe1cbf57fa1b1bd6ff97f6b0a1f87466ad89247bac59cd0a5869f6"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xserver-xorg-input-libinput-devel")
def _devel(self):
    return self.default_devel(man = True)

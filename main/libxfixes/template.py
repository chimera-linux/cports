pkgname = "libxfixes"
pkgver = "6.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xfixes library and extension of X RandR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfixes-{pkgver}.tar.bz2"
sha256 = "a7c1a24da53e0b46cac5aea79094b4b2257321c621b258729bc3139149245b4c"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxfixes-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share"])

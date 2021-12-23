pkgname = "libxpresent"
pkgver = "1.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrandr-devel"]
pkgdesc = "XPresent extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpresent-{pkgver}.tar.bz2"
sha256 = "c11ae015141a9afbe10f4f2b8ee00b11adca6373dc1b9808d7c6c138b2da7b8a"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxpresent-static")
def _static(self):
    return self.default_static()

@subpackage("libxpresent-devel")
def _devel(self):
    return self.default_devel()

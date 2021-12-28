pkgname = "libxtst"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxi-devel"]
pkgdesc = "X Tst library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXtst-{pkgver}.tar.bz2"
sha256 = "4655498a1b8e844e3d6f21f3b2c4e2b571effb5fd83199d428a6ba7ea4bf5204"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxtst-devel")
def _devel(self):
    return self.default_devel()

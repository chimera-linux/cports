pkgname = "libxft"
pkgver = "2.3.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "libxrender-devel", "freetype-devel", "fontconfig-devel"
]
pkgdesc = "X font library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXft-{pkgver}.tar.gz"
sha256 = "b7e59f69e0bbabe9438088775f7e5a7c16a572e58b11f9722519385d38192df5"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxft-devel")
def _devel(self):
    return self.default_devel()

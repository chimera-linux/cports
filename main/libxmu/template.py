pkgname = "libxmu"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxt-devel"]
pkgdesc = "X Miscellaneous Utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXmu-{pkgver}.tar.gz"
sha256 = "3091d711cdc1d8ea0f545a13b90d1464c3c3ab64778fd121f0d789b277a80289"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxmu-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

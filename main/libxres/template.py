pkgname = "libxres"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXres-{pkgver}.tar.gz"
sha256 = "8abce597ced4a7ab89032aee91f6f784d9960adc772b2b59f17e515cd4127950"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxres-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

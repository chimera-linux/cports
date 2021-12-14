pkgname = "libxres"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXres-{pkgver}.tar.bz2"
sha256 = "b6e6fb1ebb61610e56017edd928fb89a5f53b3f4f990078309877468663b2b11"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxres-static")
def _static(self):
    return self.default_static()

@subpackage("libxres-devel")
def _devel(self):
    return self.default_devel(man = True)

pkgname = "libxext"
pkgver = "1.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXext-{pkgver}.tar.bz2"
sha256 = "59ad6fcce98deaecc14d39a672cf218ca37aba617c9a0f691cac3bcd28edf82b"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxext-devel")
def _devel(self):
    return self.default_devel()

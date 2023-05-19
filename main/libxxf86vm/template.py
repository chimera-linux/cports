pkgname = "libxxf86vm"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-VidMode X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86vm-{pkgver}.tar.gz"
sha256 = "f3f1c29fef8accb0adbd854900c03c6c42f1804f2bc1e4f3ad7b2e1f3b878128"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxxf86vm-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

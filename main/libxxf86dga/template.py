pkgname = "libxxf86dga"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-DGA X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86dga-{pkgver}.tar.gz"
sha256 = "87c7482b1e29b4eeb415815641c4f69c00545a8138e1b73ff1f361f7d9c22ac4"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxxf86dga-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []

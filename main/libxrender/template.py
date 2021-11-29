pkgname = "libxrender"
pkgver = "0.9.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X Render library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrender-{pkgver}.tar.bz2"
sha256 = "c06d5979f86e64cabbde57c223938db0b939dff49fdb5a793a1d3d0396650949"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxrender-static")
def _static(self):
    return self.default_static()

@subpackage("libxrender-devel")
def _devel(self):
    return self.default_devel()

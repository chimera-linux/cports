pkgname = "libxrandr"
pkgver = "1.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxrender-devel"]
pkgdesc = "X RandR Library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrandr-{pkgver}.tar.bz2"
sha256 = "8aea0ebe403d62330bb741ed595b53741acf45033d3bda1792f1d4cc3daee023"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxrandr-static")
def _static(self):
    return self.default_static()

@subpackage("libxrandr-devel")
def _devel(self):
    return self.default_devel(man = True)

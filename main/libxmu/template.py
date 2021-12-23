pkgname = "libxmu"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxt-devel"]
pkgdesc = "X Miscellaneous Utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXmu-{pkgver}.tar.bz2"
sha256 = "9c343225e7c3dc0904f2122b562278da5fed639b1b5e880d25111561bac5b731"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxmu-static")
def _static(self):
    return self.default_static()

@subpackage("libxmu-devel")
def _devel(self):
    return self.default_devel()

pkgname = "libpng"
pkgver = "1.6.39"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for manipulating PNG images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1f4696ce70b4ee5f85f1e1623dc1229b210029fa4b7aee573df3e2ba7b036937"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []

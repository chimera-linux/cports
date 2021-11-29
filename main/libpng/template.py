pkgname = "libpng"
pkgver = "1.6.37"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for manipulating PNG images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libpng-static")
def _static(self):
    return self.default_static()

@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

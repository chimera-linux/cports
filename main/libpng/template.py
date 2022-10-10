pkgname = "libpng"
pkgver = "1.6.38"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for manipulating PNG images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b3683e8b8111ebf6f1ac004ebb6b0c975cd310ec469d98364388e9cedbfa68be"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

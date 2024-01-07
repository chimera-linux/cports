pkgname = "libpng"
pkgver = "1.6.40"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for manipulating PNG images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "535b479b2467ff231a3ec6d92a525906fb8ef27978be4f66dbe05d3f3a01b3a1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

pkgname = "libpng"
pkgver = "1.6.41"
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
sha256 = "d6a49a7a4abca7e44f72542030e53319c081fea508daccf4ecc7c6d9958d190f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

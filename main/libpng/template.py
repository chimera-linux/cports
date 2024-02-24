pkgname = "libpng"
pkgver = "1.6.43"
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
sha256 = "6a5ca0652392a2d7c9db2ae5b40210843c0bbc081cbd410825ab00cc59f14a6c"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _progs(self):
    return self.default_progs()

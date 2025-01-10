pkgname = "libpng"
pkgver = "1.6.45"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "libtool"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Library for manipulating PNG images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/libpng/libpng-{pkgver}.tar.xz"
sha256 = "926485350139ffb51ef69760db35f78846c805fef3d59bfdcb2fba704663f370"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _(self):
    return self.default_progs()

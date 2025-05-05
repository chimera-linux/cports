pkgname = "libpng"
pkgver = "1.6.48"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "libtool"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Library for manipulating PNG images"
license = "Libpng"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/libpng/libpng-{pkgver}.tar.xz"
sha256 = "46fd06ff37db1db64c0dc288d78a3f5efd23ad9ac41561193f983e20937ece03"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _(self):
    return self.default_progs()

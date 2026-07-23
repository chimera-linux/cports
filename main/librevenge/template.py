pkgname = "librevenge"
pkgver = "0.0.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror", "--disable-static"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["boost-devel", "zlib-ng-compat-devel", "cppunit-devel"]
pkgdesc = "Library for reverse engineered format filters"
license = "MPL-2.0"
url = "https://sourceforge.net/p/libwpd/librevenge"
source = f"$(SOURCEFORGE_SITE)/libwpd/librevenge-{pkgver}.tar.xz"
sha256 = "19eacf5ce55d7fe6a990a45142589cdf7da0c7b68701797f133482cb44f189fa"


@subpackage("librevenge-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()

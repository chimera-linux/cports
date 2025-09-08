pkgname = "librevenge"
pkgver = "0.0.5"
pkgrel = 8
build_style = "gnu_configure"
configure_args = ["--disable-werror", "--disable-static"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["boost-devel", "zlib-ng-compat-devel", "cppunit-devel"]
pkgdesc = "Library for reverse engineered format filters"
license = "MPL-2.0"
url = "https://sourceforge.net/p/libwpd/librevenge"
source = f"$(SOURCEFORGE_SITE)/libwpd/librevenge-{pkgver}.tar.xz"
sha256 = "106d0c44bb6408b1348b9e0465666fa83b816177665a22cd017e886c1aaeeb34"


@subpackage("librevenge-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()

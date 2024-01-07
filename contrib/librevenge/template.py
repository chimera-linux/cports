pkgname = "librevenge"
pkgver = "0.0.5"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-werror", "--disable-static"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
makedepends = ["boost-devel", "zlib-devel", "cppunit-devel"]
pkgdesc = "Library for reverse engineered format filters"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://sourceforge.net/p/libwpd/librevenge"
source = f"$(SOURCEFORGE_SITE)/libwpd/{pkgname}-{pkgver}.tar.xz"
sha256 = "106d0c44bb6408b1348b9e0465666fa83b816177665a22cd017e886c1aaeeb34"


@subpackage("librevenge-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

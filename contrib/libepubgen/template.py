pkgname = "libepubgen"
pkgver = "0.1.1"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "libxml2-devel"]
checkdepends = ["cppunit-devel"]
pkgdesc = "EPUB generator for librevenge"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://sourceforge.net/projects/libepubgen"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "03e084b994cbeffc8c3dd13303b2cb805f44d8f2c3b79f7690d7e3fc7f6215ad"


@subpackage("libepubgen-devel")
def _devel(self):
    return self.default_devel()

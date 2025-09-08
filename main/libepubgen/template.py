pkgname = "libepubgen"
pkgver = "0.1.1"
pkgrel = 7
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel", "libxml2-devel"]
checkdepends = ["cppunit-devel"]
pkgdesc = "EPUB generator for librevenge"
license = "MPL-2.0"
url = "https://sourceforge.net/projects/libepubgen"
source = f"$(SOURCEFORGE_SITE)/libepubgen/libepubgen-{pkgver}/libepubgen-{pkgver}.tar.xz"
sha256 = "03e084b994cbeffc8c3dd13303b2cb805f44d8f2c3b79f7690d7e3fc7f6215ad"


@subpackage("libepubgen-devel")
def _(self):
    return self.default_devel()

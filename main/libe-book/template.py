pkgname = "libe-book"
pkgver = "0.1.4"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gperf",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "liblangtag-devel",
    "librevenge-devel",
    "libxml2-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "Import reflowable e-book formats"
license = "MPL-2.0"
url = "https://sourceforge.net/projects/libebook"
source = f"$(SOURCEFORGE_SITE)/project/libebook/libe-book-{pkgver}/libe-book-{pkgver}.tar.xz"
sha256 = "104b7e791b6632745898e9b6a0037b7540235771a4d8c3bde2c764466ad912f1"


@subpackage("libe-book-progs")
def _(self):
    return self.default_progs()


@subpackage("libe-book-devel")
def _(self):
    return self.default_devel()

pkgname = "libe-book"
pkgver = "0.1.3"
pkgrel = 13
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
sha256 = "7e8d8ff34f27831aca3bc6f9cc532c2f90d2057c778963b884ff3d1e34dfe1f9"


@subpackage("libe-book-progs")
def _(self):
    return self.default_progs()


@subpackage("libe-book-devel")
def _(self):
    return self.default_devel()

pkgname = "libvisio"
pkgver = "0.1.7"
pkgrel = 6
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gperf",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "librevenge-devel",
    "libxml2-devel",
]
pkgdesc = "Library for reading and converting MS Visio diagrams"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libvisio"
source = f"http://dev-www.libreoffice.org/src/libvisio-{pkgver}.tar.xz"
sha256 = "8faf8df870cb27b09a787a1959d6c646faa44d0d8ab151883df408b7166bea4c"


@subpackage("libvisio-progs")
def _(self):
    return self.default_progs()


@subpackage("libvisio-devel")
def _(self):
    return self.default_devel()

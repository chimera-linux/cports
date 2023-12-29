pkgname = "libvisio"
pkgver = "0.1.7"
pkgrel = 3
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "perl", "gperf"]
makedepends = ["libxml2-devel", "icu-devel", "librevenge-devel", "boost-devel"]
pkgdesc = "Library for reading and converting MS Visio diagrams"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libvisio"
source = f"http://dev-www.libreoffice.org/src/{pkgname}-{pkgver}.tar.xz"
sha256 = "8faf8df870cb27b09a787a1959d6c646faa44d0d8ab151883df408b7166bea4c"


@subpackage("libvisio-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libvisio-devel")
def _devel(self):
    return self.default_devel()

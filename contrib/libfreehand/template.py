pkgname = "libfreehand"
pkgver = "0.1.2"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "gperf"]
makedepends = [
    "lcms2-devel",
    "icu-devel",
    "librevenge-devel",
    "boost-devel",
    "lcms2-devel",
]
pkgdesc = "Parser for Aldus/Macromedia/Adobe FreeHand documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libfreehand"
source = (
    f"http://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "0e422d1564a6dbf22a9af598535425271e583514c0f7ba7d9091676420de34ac"


@subpackage("libfreehand-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libfreehand-devel")
def _devel(self):
    return self.default_devel()

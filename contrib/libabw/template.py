pkgname = "libabw"
pkgver = "0.1.3"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "gperf", "perl"]
makedepends = ["librevenge-devel", "boost-devel", "libxml2-devel"]
pkgdesc = "Library for AbiWord document format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libabw"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "e763a9dc21c3d2667402d66e202e3f8ef4db51b34b79ef41f56cacb86dcd6eed"


@subpackage("libabw-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libabw-devel")
def _devel(self):
    return self.default_devel()

pkgname = "libqxp"
pkgver = "0.0.2"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "icu-devel"]
pkgdesc = "Library for QuarkXPress format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libqxp"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "e137b6b110120a52c98edd02ebdc4095ee08d0d5295a94316a981750095a945c"


@subpackage("libqxp-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libqxp-devel")
def _devel(self):
    return self.default_devel()

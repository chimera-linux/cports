pkgname = "libpagemaker"
pkgver = "0.0.4"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel"]
pkgdesc = "Library for Aldus/Adobe PageMaker format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libpagemaker"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "66adacd705a7d19895e08eac46d1e851332adf2e736c566bef1164e7a442519d"


@subpackage("libpagemaker-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libpagemaker-devel")
def _devel(self):
    return self.default_devel()

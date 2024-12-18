pkgname = "libpagemaker"
pkgver = "0.0.4"
pkgrel = 5
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel"]
pkgdesc = "Library for Aldus/Adobe PageMaker format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libpagemaker"
source = f"https://dev-www.libreoffice.org/src/libpagemaker/libpagemaker-{pkgver}.tar.xz"
sha256 = "66adacd705a7d19895e08eac46d1e851332adf2e736c566bef1164e7a442519d"


@subpackage("libpagemaker-progs")
def _(self):
    return self.default_progs()


@subpackage("libpagemaker-devel")
def _(self):
    return self.default_devel()

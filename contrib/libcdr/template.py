pkgname = "libcdr"
pkgver = "0.1.7"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-debug"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["lcms2-devel", "icu-devel", "librevenge-devel", "boost-devel"]
pkgdesc = "Corel Draw format importer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libcdr"
source = (
    f"http://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
)
sha256 = "ae613caeb7e0e539cbc1b08ea5169bddaed8d2021d25ef66b39ddc0aa72c2902"


@subpackage("libcdr-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libcdr-devel")
def _devel(self):
    self.depends += ["boost-devel"]

    return self.default_devel()

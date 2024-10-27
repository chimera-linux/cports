pkgname = "libcdr"
pkgver = "0.1.7"
pkgrel = 7
build_style = "gnu_configure"
configure_args = ["--disable-debug"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["lcms2-devel", "icu-devel", "librevenge-devel", "boost-devel"]
pkgdesc = "Corel Draw format importer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libcdr"
source = f"http://dev-www.libreoffice.org/src/libcdr/libcdr-{pkgver}.tar.bz2"
sha256 = "ae613caeb7e0e539cbc1b08ea5169bddaed8d2021d25ef66b39ddc0aa72c2902"


@subpackage("libcdr-progs")
def _(self):
    return self.default_progs()


@subpackage("libcdr-devel")
def _(self):
    self.depends += ["boost-devel"]

    return self.default_devel()

pkgname = "rasqal"
pkgver = "0.9.33"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool", "gtk-doc-tools"]
makedepends = ["mpfr-devel", "raptor-devel"]
checkdepends = ["perl"]
pkgdesc = "RDF Query Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR Apache-2.0"
url = "https://librdf.org/rasqal"
source = f"https://librdf.org/dist/source/{pkgname}-{pkgver}.tar.gz"
sha256 = "6924c9ac6570bd241a9669f83b467c728a322470bf34f4b2da4f69492ccfd97c"


@subpackage("rasqal-devel")
def _devel(self):
    return self.default_devel()

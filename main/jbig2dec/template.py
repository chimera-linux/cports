# AGPL: forbidden from being a dependency except in special unambiguous cases
pkgname = "jbig2dec"
pkgver = "0.19"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libpng-devel"]
checkdepends = ["python"]
pkgdesc = "JBIG2 decoder library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "AGPL-3.0-or-later"
url = "https://www.jbig2dec.com"
source = f"https://github.com/ArtifexSoftware/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "e81b787ad0b147a437a52d9ce7de1a8f429655e8aa030383b6b2dd8919373717"
# FIXME int
hardening = ["!int"]


@subpackage("jbig2dec-devel")
def _devel(self):
    return self.default_devel()


@subpackage("jbig2dec-progs")
def _xmlwf(self):
    return self.default_progs()

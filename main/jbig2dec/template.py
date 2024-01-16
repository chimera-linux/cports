# AGPL: forbidden from being a dependency except in special unambiguous cases
pkgname = "jbig2dec"
pkgver = "0.20"
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
source = f"https://github.com/ArtifexSoftware/jbig2dec/archive/{pkgver}.tar.gz"
sha256 = "a9705369a6633aba532693450ec802c562397e1b824662de809ede92f67aff21"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("jbig2dec-devel")
def _devel(self):
    return self.default_devel()


@subpackage("jbig2dec-progs")
def _xmlwf(self):
    return self.default_progs()

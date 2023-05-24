pkgname = "gsl"
pkgver = "2.7.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "GNU Scientific Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gsl/gsl.html"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "dcb0fbd43048832b757ff9942691a8dd70026d5da0ff85601e52687f6deeb34b"
# FIXME fails tests
hardening = ["!int"]
# fails on x86_64, passes elsewhere, takes a long time
options = ["!check"]


@subpackage("gsl-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

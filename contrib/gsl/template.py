pkgname = "gsl"
pkgver = "2.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "GNU Scientific Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gsl/gsl.html"
source = f"$(GNU_SITE)/gsl/gsl-{pkgver}.tar.gz"
sha256 = "6a99eeed15632c6354895b1dd542ed5a855c0f15d9ad1326c6fe2b2c9e423190"
# FIXME fails tests
hardening = ["!int"]
# fails on x86_64, passes elsewhere, takes a long time
options = ["!check"]


@subpackage("gsl-devel")
def _(self):
    return self.default_devel()

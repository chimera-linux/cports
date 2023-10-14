pkgname = "librtas"
pkgver = "2.0.5"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "pkgconf", "gmake"]
makedepends = ["linux-headers"]
pkgdesc = "Librtas library for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibm-power-utilities/librtas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b4928b300350c12618563a051be01189275853fd8eacaac509c9aa1460991ec4"


@subpackage("librtas-devel")
def _devel(self):
    return self.default_devel()

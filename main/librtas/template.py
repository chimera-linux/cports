pkgname = "librtas"
pkgver = "2.0.6"
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
sha256 = "b88ca9ac5acafb924cd0aaf56c89a7f149c84ade0fc6840f3ef8356ab96a1254"


@subpackage("librtas-devel")
def _devel(self):
    return self.default_devel()

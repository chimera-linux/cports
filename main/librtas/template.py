pkgname = "librtas"
pkgver = "2.0.6"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Librtas library for Linux on Power systems"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibm-power-utilities/librtas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b88ca9ac5acafb924cd0aaf56c89a7f149c84ade0fc6840f3ef8356ab96a1254"


@subpackage("librtas-devel")
def _(self):
    return self.default_devel()

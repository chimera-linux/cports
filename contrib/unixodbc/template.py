pkgname = "unixodbc"
pkgver = "2.3.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libltdl-devel", "libedit-readline-devel"]
pkgdesc = "Unix ODBC implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://www.unixodbc.org"
source = f"{url}/unixODBC-{pkgver}.tar.gz"
sha256 = "d9e55c8e7118347e3c66c87338856dad1516b490fb7c756c1562a2c267c73b5c"


@subpackage("unixodbc-libs")
def _libs(self):
    return self.default_libs()


@subpackage("unixodbc-devel")
def _dev(self):
    return self.default_devel()

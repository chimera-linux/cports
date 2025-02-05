pkgname = "unixodbc"
pkgver = "2.3.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libtool-devel", "libedit-readline-devel"]
pkgdesc = "Unix ODBC implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://www.unixodbc.org"
source = f"{url}/unixODBC-{pkgver}.tar.gz"
sha256 = "f210501445ce21bf607ba51ef8c125e10e22dffdffec377646462df5f01915ec"


@subpackage("unixodbc-libs")
def _(self):
    return self.default_libs()


@subpackage("unixodbc-devel")
def _(self):
    return self.default_devel()

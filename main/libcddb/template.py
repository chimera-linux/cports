pkgname = "libcddb"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "slibtool"]
pkgdesc = "Library to access data on a CDDB server"
license = "LGPL-2.0-or-later"
url = "http://libcddb.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/libcddb/libcddb-{pkgver}.tar.gz"
sha256 = "68e9b53918b9bea727fb2db78936526671c039dcd7396cb82ecd6854e866048c"
# attempts to contact a cddb server
options = ["!check"]


@subpackage("libcddb-devel")
def _(self):
    return self.default_devel()


@subpackage("libcddb-progs")
def _(self):
    return self.default_progs()

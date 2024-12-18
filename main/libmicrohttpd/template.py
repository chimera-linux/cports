pkgname = "libmicrohttpd"
pkgver = "1.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["gnutls-devel", "linux-headers"]
checkdepends = ["curl-devel"]
pkgdesc = "HTTP server library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libmicrohttpd"
source = f"$(GNU_SITE)/libmicrohttpd/libmicrohttpd-{pkgver}.tar.gz"
sha256 = "a89e09fc9b4de34dde19f4fcb4faaa1ce10299b9908db1132bbfa1de47882b94"


@subpackage("libmicrohttpd-devel")
def _(self):
    return self.default_devel()

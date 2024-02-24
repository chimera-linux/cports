pkgname = "libunistring"
pkgver = "1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
pkgdesc = "Library for manipulating Unicode strings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.gnu.org/software/libunistring"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fd6d5662fa706487c48349a758b57bc149ce94ec6c30624ec9fdc473ceabbc8e"


@subpackage("libunistring-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share"])

pkgname = "libunistring"
pkgver = "1.1"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Library for manipulating Unicode strings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.gnu.org/software/libunistring"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a2252beeec830ac444b9f68d6b38ad883db19919db35b52222cf827c385bdb6a"


@subpackage("libunistring-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share"])


configure_gen = []

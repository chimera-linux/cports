pkgname = "libunistring"
pkgver = "1.0"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Library for manipulating Unicode strings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.gnu.org/software/libunistring"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3c0184c0e492d7c208ce31d25dd1d2c58f0c3ed6cbbe032c5b248cddad318544"

@subpackage("libunistring-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share"])

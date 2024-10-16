pkgname = "libunistring"
pkgver = "1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
pkgdesc = "Library for manipulating Unicode strings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.gnu.org/software/libunistring"
source = f"$(GNU_SITE)/libunistring/libunistring-{pkgver}.tar.gz"
sha256 = "8ea8ccf86c09dd801c8cac19878e804e54f707cf69884371130d20bde68386b7"


@subpackage("libunistring-devel")
def _(self):
    return self.default_devel(extra=["usr/share"])

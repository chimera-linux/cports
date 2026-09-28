pkgname = "libunistring"
pkgver = "1.4.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
pkgdesc = "Library for manipulating Unicode strings"
license = "LGPL-3.0-or-later"
url = "http://www.gnu.org/software/libunistring"
source = f"$(GNU_SITE)/libunistring/libunistring-{pkgver}.tar.gz"
sha256 = "e82664b170064e62331962126b259d452d53b227bb4a93ab20040d846fec01d8"


@subpackage("libunistring-devel")
def _(self):
    return self.default_devel(extra=["usr/share"])

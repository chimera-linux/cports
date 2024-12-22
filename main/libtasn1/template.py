pkgname = "libtasn1"
pkgver = "4.19.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "gtk-doc-tools", "pkgconf", "perl", "slibtool"]
pkgdesc = "ASN.1 structure parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libtasn1"
source = f"$(GNU_SITE)/libtasn1/libtasn1-{pkgver}.tar.gz"
sha256 = "1613f0ac1cf484d6ec0ce3b8c06d56263cc7242f1c23b30d82d23de345a63f7a"


@subpackage("libtasn1-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libtasn1-progs")
def _(self):
    return self.default_progs()

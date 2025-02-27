pkgname = "libtasn1"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gtk-doc-tools", "pkgconf", "perl", "slibtool"]
pkgdesc = "ASN.1 structure parser library"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libtasn1"
source = f"$(GNU_SITE)/libtasn1/libtasn1-{pkgver}.tar.gz"
sha256 = "92e0e3bd4c02d4aeee76036b2ddd83f0c732ba4cda5cb71d583272b23587a76c"


@subpackage("libtasn1-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libtasn1-progs")
def _(self):
    return self.default_progs()

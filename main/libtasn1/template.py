pkgname = "libtasn1"
pkgver = "4.21.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "perl",
    "pkgconf",
    "slibtool",
    "texinfo",
]
pkgdesc = "ASN.1 structure parser library"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libtasn1"
source = f"$(GNU_SITE)/libtasn1/libtasn1-{pkgver}.tar.gz"
sha256 = "1d8a444a223cc5464240777346e125de51d8e6abf0b8bac742ac84609167dc87"


@subpackage("libtasn1-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])


@subpackage("libtasn1-progs")
def _(self):
    return self.default_progs()

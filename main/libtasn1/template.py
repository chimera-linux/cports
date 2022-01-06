pkgname = "libtasn1"
pkgver = "4.18.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "perl"]
pkgdesc = "ASN.1 structure parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libtasn1"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "4365c154953563d64c67a024b607d1ee75c6db76e0d0f65709ea80a334cd1898"

@subpackage("libtasn1-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/info"])

@subpackage("libtasn1-progs")
def _progs(self):
    return self.default_progs()

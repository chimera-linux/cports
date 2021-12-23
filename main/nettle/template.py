pkgname = "nettle"
pkgver = "3.7.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-mini-gmp"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "texinfo", "bsdm4"]
makedepends = ["linux-headers"]
pkgdesc = "Low-level cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "661f5eb03f048a3b924c3a8ad2515d4068e40f67e774e8a26827658007e3bcf0"

@subpackage("nettle-static")
def _static(self):
    return self.default_static()

@subpackage("nettle-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/info"])

@subpackage("nettle-progs")
def _progs(self):
    return self.default_progs()

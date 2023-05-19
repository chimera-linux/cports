pkgname = "nettle"
pkgver = "3.8.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "texinfo"]
makedepends = ["gmp-devel", "linux-headers"]
pkgdesc = "Low-level cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "364f3e2b77cd7dcde83fd7c45219c834e54b0c75e428b6f894a23d12dd41cbfe"

@subpackage("nettle-devel")
def _devel(self):
    self.depends += ["gmp-devel"]

    return self.default_devel(extra = ["usr/share/info"])

@subpackage("nettle-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []

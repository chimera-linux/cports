pkgname = "nettle"
pkgver = "3.9.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "texinfo", "automake", "libtool"]
makedepends = ["gmp-devel", "linux-headers"]
pkgdesc = "Low-level cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ccfeff981b0ca71bbd6fbcb054f407c60ffb644389a5be80d6716d5b550c6ce3"


@subpackage("nettle-devel")
def _devel(self):
    self.depends += ["gmp-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("nettle-progs")
def _progs(self):
    return self.default_progs()

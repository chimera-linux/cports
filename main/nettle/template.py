pkgname = "nettle"
pkgver = "3.10"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "texinfo", "automake", "libtool"]
makedepends = ["gmp-devel", "linux-headers"]
pkgdesc = "Low-level cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/nettle/nettle-{pkgver}.tar.gz"
sha256 = "b4c518adb174e484cb4acea54118f02380c7133771e7e9beb98a0787194ee47c"


@subpackage("nettle-devel")
def _(self):
    self.depends += ["gmp-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("nettle-progs")
def _(self):
    return self.default_progs()

pkgname = "nettle"
pkgver = "3.10.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "texinfo", "automake", "libtool"]
makedepends = ["gmp-devel", "linux-headers"]
pkgdesc = "Low-level cryptographic library"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/nettle/nettle-{pkgver}.tar.gz"
sha256 = "fe9ff51cb1f2abb5e65a6b8c10a92da0ab5ab6eaf26e7fc2b675c45f1fb519b5"


@subpackage("nettle-devel")
def _(self):
    self.depends += ["gmp-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("nettle-progs")
def _(self):
    return self.default_progs()

pkgname = "nettle"
pkgver = "3.10.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "texinfo", "automake", "libtool"]
makedepends = ["gmp-devel", "linux-headers"]
pkgdesc = "Low-level cryptographic library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://www.lysator.liu.se/~nisse/nettle"
source = f"$(GNU_SITE)/nettle/nettle-{pkgver}.tar.gz"
sha256 = "b0fcdd7fc0cdea6e80dcf1dd85ba794af0d5b4a57e26397eee3bc193272d9132"


@subpackage("nettle-devel")
def _(self):
    self.depends += ["gmp-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("nettle-progs")
def _(self):
    return self.default_progs()

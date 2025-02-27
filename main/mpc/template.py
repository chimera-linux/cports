pkgname = "mpc"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["gmp-devel", "mpfr-devel"]
pkgdesc = "C library for complex numbers"
license = "LGPL-3.0-or-later"
url = "https://www.multiprecision.org/mpc"
source = f"$(GNU_SITE)/mpc/mpc-{pkgver}.tar.gz"
sha256 = "ab642492f5cf882b74aa0cb730cd410a81edcdbec895183ce930e706c1c759b8"


@subpackage("mpc-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel(extra=["usr/share"])

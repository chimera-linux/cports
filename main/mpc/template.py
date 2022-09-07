pkgname = "mpc"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["gmp-devel", "mpfr-devel"]
pkgdesc = "C library for complex numbers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://www.multiprecision.org/mpc"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "17503d2c395dfcf106b622dc142683c1199431d095367c6aacba6eec30340459"

@subpackage("mpc-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel(extra = ["usr/share"])

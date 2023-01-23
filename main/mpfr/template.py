pkgname = "mpfr"
pkgver = "4.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-thread-safe"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["gmp-devel"]
pkgdesc = "Library for multiple-precision floating-point computations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://www.mpfr.org"
source = f"{url}/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0c98a3f1732ff6ca4ea690552079da9c597872d30e96ec28414ee23c95558a7f"

@subpackage("mpfr-devel")
def _devel(self):
    self.depends += ["gmp-devel"]

    return self.default_devel()

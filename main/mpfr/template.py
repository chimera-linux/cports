pkgname = "mpfr"
pkgver = "4.2.1"
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
sha256 = "277807353a6726978996945af13e52829e3abd7a9a5b7fb2793894e18f1fcbb2"


@subpackage("mpfr-devel")
def _devel(self):
    self.depends += ["gmp-devel"]

    return self.default_devel()


configure_gen = []

pkgname = "mpfr"
pkgver = "4.2.0"
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
sha256 = "06a378df13501248c1b2db5aa977a2c8126ae849a9d9b7be2546fb4a9c26d993"

@subpackage("mpfr-devel")
def _devel(self):
    self.depends += ["gmp-devel"]

    return self.default_devel()

configure_gen = []

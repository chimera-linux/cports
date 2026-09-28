pkgname = "mpfr"
pkgver = "4.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-thread-safe"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "texinfo"]
makedepends = ["gmp-devel"]
pkgdesc = "Library for multiple-precision floating-point computations"
license = "LGPL-3.0-or-later"
url = "https://www.mpfr.org"
source = f"{url}/mpfr-{pkgver}/mpfr-{pkgver}.tar.xz"
sha256 = "b67ba0383ef7e8a8563734e2e889ef5ec3c3b898a01d00fa0a6869ad81c6ce01"


@subpackage("mpfr-devel")
def _(self):
    self.depends += ["gmp-devel"]

    return self.default_devel()

pkgname = "gmp"
pkgver = "6.3.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-cxx"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Library for arbitrary precision arithmetic"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later OR GPL-2.0-or-later"
url = "https://gmplib.org"
source = f"{url}/download/gmp/gmp-{pkgver}.tar.xz"
sha256 = "a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898"


@subpackage("gmp-gmpxx")
def _(self):
    self.subdesc = "C++ support"
    # transitional
    self.provides = [self.with_pkgver("gmpxx")]

    return ["usr/lib/libgmpxx.so.*"]


@subpackage("gmp-gmpxx-devel")
def _(self):
    self.subdesc = "C++ development files"
    # transitional
    self.provides = [self.with_pkgver("gmpxx-devel")]

    return [
        "usr/include/gmpxx.h",
        "usr/lib/libgmpxx.*",
        "usr/lib/pkgconfig/gmpxx.pc",
    ]


@subpackage("gmp-devel")
def _(self):
    return self.default_devel()

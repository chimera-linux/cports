pkgname = "gmp"
pkgver = "6.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx"]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for arbitrary precision arithmetic"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later OR GPL-2.0-or-later"
url = "https://gmplib.org"
source = f"{url}/download/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898"


@subpackage("gmpxx")
def _cxx(self):
    self.pkgdesc = f"{pkgdesc} (C++ support)"

    return ["usr/lib/libgmpxx.so.*"]


@subpackage("gmpxx-devel")
def _cxxdevel(self):
    self.pkgdesc = f"{pkgdesc} (C++ development files)"

    return [
        "usr/include/gmpxx.h",
        "usr/lib/libgmpxx.*",
        "usr/lib/pkgconfig/gmpxx.pc",
    ]


@subpackage("gmp-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

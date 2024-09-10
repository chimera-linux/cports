pkgname = "libbytesize"
pkgver = "2.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = ["gmp-devel", "mpfr-devel", "pcre2-devel"]
pkgdesc = "Library for operations with sizes in bytes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libbytesize"
source = f"{url}/releases/download/{pkgver}/libbytesize-{pkgver}.tar.gz"
sha256 = "1f6ce157750ed1201ce83edd3c23d997a615c7da30f9a0e5bb44635f66768d81"


@subpackage("libbytesize-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libbytesize-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*", "cmd:bscalc"]

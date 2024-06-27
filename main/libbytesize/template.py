pkgname = "libbytesize"
pkgver = "2.10"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext",
    "gmake",
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
sha256 = "1d1ce3be8ac59fd59511d0794c7327d5cf33f1e83496837b17e19ac49400cad1"


@subpackage("libbytesize-devel")
def _devel(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libbytesize-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]

pkgname = "libbytesize"
pkgver = "2.12"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libbytesize"
source = f"{url}/releases/download/{pkgver}/libbytesize-{pkgver}.tar.gz"
sha256 = "8356bac2cafd2f31f39bf1ad373cef8448cab08b817aeaee5c526d54e81c3c5a"


@subpackage("libbytesize-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libbytesize-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*", "usr/bin/bscalc", "usr/share/man/man1/bscalc.1"]

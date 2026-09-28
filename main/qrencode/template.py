pkgname = "qrencode"
pkgver = "4.1.1"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--with-tests"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpng-devel"]
pkgdesc = "Library for encoding QR codes"
license = "LGPL-2.1-or-later"
url = "https://fukuchi.org/works/qrencode/index.html.en"
source = (
    f"https://github.com/fukuchi/libqrencode/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c"


@subpackage("qrencode-devel")
def _(self):
    return self.default_devel()


@subpackage("qrencode-progs")
def _(self):
    return self.default_progs()

pkgname = "qrencode"
pkgver = "4.1.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-tests"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpng-devel"]
pkgdesc = "Library for encoding QR codes"
license = "LGPL-2.1-or-later"
url = "https://fukuchi.org/works/qrencode/index.html.en"
source = f"https://fukuchi.org/works/qrencode/qrencode-{pkgver}.tar.bz2"
sha256 = "e455d9732f8041cf5b9c388e345a641fd15707860f928e94507b1961256a6923"


@subpackage("qrencode-devel")
def _(self):
    return self.default_devel()


@subpackage("qrencode-progs")
def _(self):
    return self.default_progs()

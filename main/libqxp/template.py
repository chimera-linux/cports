pkgname = "libqxp"
pkgver = "0.0.2"
pkgrel = 11
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel", "icu-devel"]
pkgdesc = "Library for QuarkXPress format"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libqxp"
source = f"https://dev-www.libreoffice.org/src/libqxp/libqxp-{pkgver}.tar.xz"
sha256 = "e137b6b110120a52c98edd02ebdc4095ee08d0d5295a94316a981750095a945c"


@subpackage("libqxp-progs")
def _(self):
    return self.default_progs()


@subpackage("libqxp-devel")
def _(self):
    return self.default_devel()

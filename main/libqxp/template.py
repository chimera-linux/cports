pkgname = "libqxp"
pkgver = "0.0.3"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel", "icu-devel"]
pkgdesc = "Library for QuarkXPress format"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libqxp"
source = f"https://dev-www.libreoffice.org/src/libqxp/libqxp-{pkgver}.tar.xz"
sha256 = "4687a9cc96c32d7406e5072c4da150fca696c563e5cde62b024f82fa53d32332"


@subpackage("libqxp-progs")
def _(self):
    return self.default_progs()


@subpackage("libqxp-devel")
def _(self):
    return self.default_devel()

pkgname = "libvisio"
pkgver = "0.1.8"
pkgrel = 6
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gperf",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "librevenge-devel",
    "libxml2-devel",
]
pkgdesc = "Library for reading and converting MS Visio diagrams"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libvisio"
source = f"http://dev-www.libreoffice.org/src/libvisio-{pkgver}.tar.xz"
sha256 = "b4098ffbf4dcb9e71213fa0acddbd928f27bed30db2d80234813b15d53d0405b"


@subpackage("libvisio-progs")
def _(self):
    return self.default_progs()


@subpackage("libvisio-devel")
def _(self):
    return self.default_devel()

pkgname = "libvisio"
pkgver = "0.1.11"
pkgrel = 0
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
sha256 = "2a6efd40b6d9dbcb70fba3be53112366882ba97b57151df3698dfa478c8d8dd3"


@subpackage("libvisio-progs")
def _(self):
    return self.default_progs()


@subpackage("libvisio-devel")
def _(self):
    return self.default_devel()

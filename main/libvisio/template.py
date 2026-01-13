pkgname = "libvisio"
pkgver = "0.1.10"
pkgrel = 1
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
sha256 = "9e9eff75112d4d92d92262ad7fc2599c21e26f8fc5ba54900efdc83c0501e472"


@subpackage("libvisio-progs")
def _(self):
    return self.default_progs()


@subpackage("libvisio-devel")
def _(self):
    return self.default_devel()

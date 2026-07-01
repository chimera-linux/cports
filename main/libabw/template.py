pkgname = "libabw"
pkgver = "0.1.4"
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
makedepends = ["librevenge-devel", "boost-devel", "libxml2-devel"]
pkgdesc = "Library for AbiWord document format"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libabw"
source = f"https://dev-www.libreoffice.org/src/libabw/libabw-{pkgver}.tar.xz"
sha256 = "fa2685a3440da6e03a66a778480d93cb95f6064e4541e58e37397680760fd6a0"


@subpackage("libabw-progs")
def _(self):
    return self.default_progs()


@subpackage("libabw-devel")
def _(self):
    return self.default_devel()

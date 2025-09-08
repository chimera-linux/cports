pkgname = "libabw"
pkgver = "0.1.3"
pkgrel = 7
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
sha256 = "e763a9dc21c3d2667402d66e202e3f8ef4db51b34b79ef41f56cacb86dcd6eed"


@subpackage("libabw-progs")
def _(self):
    return self.default_progs()


@subpackage("libabw-devel")
def _(self):
    return self.default_devel()

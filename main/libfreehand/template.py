pkgname = "libfreehand"
pkgver = "0.1.2"
pkgrel = 7
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gperf",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "lcms2-devel",
    "lcms2-devel",
    "librevenge-devel",
]
pkgdesc = "Parser for Aldus/Macromedia/Adobe FreeHand documents"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libfreehand"
source = f"http://dev-www.libreoffice.org/src/libfreehand/libfreehand-{pkgver}.tar.xz"
sha256 = "0e422d1564a6dbf22a9af598535425271e583514c0f7ba7d9091676420de34ac"


@subpackage("libfreehand-progs")
def _(self):
    return self.default_progs()


@subpackage("libfreehand-devel")
def _(self):
    return self.default_devel()

pkgname = "libfreehand"
pkgver = "0.1.3"
pkgrel = 0
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
sha256 = "a431d78767e5aa27ade7c6d1b7a11a9f1848cb4b9260bf0a6a44689553ecccfe"


@subpackage("libfreehand-progs")
def _(self):
    return self.default_progs()


@subpackage("libfreehand-devel")
def _(self):
    return self.default_devel()

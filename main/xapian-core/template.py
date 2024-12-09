pkgname = "xapian-core"
pkgver = "1.4.27"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "zlib-ng-compat-devel",
]
pkgdesc = "Open source search engine library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xapian.org"
source = f"https://oligarchy.co.uk/xapian/{pkgver}/xapian-core-{pkgver}.tar.xz"
sha256 = "bcbc99cfbf16080119c2571fc296794f539bd542ca3926f17c2999600830ab61"
hardening = ["vis", "cfi"]
# see below
options = []

if self.profile().arch == "ppc64":
    # FIXME: hangs after replacedoc9
    options += ["!check"]


@subpackage("xapian-core-devel")
def _(self):
    return self.default_devel()


@subpackage("xapian-core-libs")
def _(self):
    return self.default_libs()

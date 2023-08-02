pkgname = "xapian-core"
pkgver = "1.4.23"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "zlib-devel",
]
pkgdesc = "Open source search engine library"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://xapian.org"
source = f"https://oligarchy.co.uk/xapian/{pkgver}/xapian-core-{pkgver}.tar.xz"
sha256 = "30d3518172084f310dab86d262b512718a7f9a13635aaa1a188e61dc26b2288c"
hardening = ["vis", "cfi"]


@subpackage("xapian-core-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xapian-core-libs")
def _libs(self):
    return self.default_libs()

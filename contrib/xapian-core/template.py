pkgname = "xapian-core"
pkgver = "1.4.25"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = [
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
sha256 = "0c99dfdd817571cb5689bc412a7e021407938313f38ea3a70fa3bf86410608ee"
hardening = ["vis", "cfi"]
# see below
options = []

if self.profile().arch == "ppc64":
    # FIXME: hangs after replacedoc9
    options += ["!check"]


@subpackage("xapian-core-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xapian-core-libs")
def _libs(self):
    return self.default_libs()

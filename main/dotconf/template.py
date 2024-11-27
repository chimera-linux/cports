pkgname = "dotconf"
pkgver = "1.4.1"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Dot.conf configuration file parser library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only AND Apache-1.1"
url = "https://github.com/williamh/dotconf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5922c46cacf99b2ecc4853d28a2bda4a489292e73276e604bd9cba29dfca892d"


@subpackage("dotconf-devel")
def _(self):
    return self.default_devel()

pkgname = "liborcus"
pkgver = "0.19.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "python"]
makedepends = [
    "boost-devel",
    "ixion-devel",
    "python-devel",
    "zlib-devel",
    "mdds",
]
pkgdesc = "Library for processing spreadsheets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/orcus/orcus"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "93be2cdd53b77816c3672f59308d023422029848b74d865cd3c0c68e73f31512"


@subpackage("liborcus-progs")
def _libs(self):
    return self.default_progs()


@subpackage("liborcus-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]


@subpackage("liborcus-devel")
def _devel(self):
    return self.default_devel()

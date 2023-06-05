pkgname = "liborcus"
pkgver = "0.18.1"
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
sha256 = "f759b9c79e1e865b39b16f0f222bc9bde9b8494e02aae4559db4053f95001e76"


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

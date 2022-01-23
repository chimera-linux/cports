pkgname = "newt"
pkgver = "0.52.21"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "python-devel"]
makedepends = ["python-devel", "slang-devel", "popt-devel"]
pkgdesc = "Library for color text mode, widget based user interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-only"
url = "https://pagure.io/newt"
source = f"https://pagure.io/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "265eb46b55d7eaeb887fca7a1d51fe115658882dfe148164b6c49fccac5abb31"
# no proper check target
options = ["!check"]

@subpackage("newt-devel")
def _devel(self):
    return self.default_devel()

@subpackage("newt-python")
def _progs(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]

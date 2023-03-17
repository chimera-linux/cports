pkgname = "newt"
pkgver = "0.52.23"
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
sha256 = "caa372907b14ececfe298f0d512a62f41d33b290610244a58aed07bbc5ada12a"
# no proper check target
options = ["!check"]

@subpackage("newt-devel")
def _devel(self):
    return self.default_devel()

@subpackage("newt-python")
def _progs(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]

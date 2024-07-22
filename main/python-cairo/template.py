pkgname = "python-cairo"
pkgver = "1.26.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["cairo-devel", "python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Cairo graphics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "a11b999ce55b798dbf13516ab038e0ce8b6ec299b208d7c4e767a6f7e68e8430"


@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()

pkgname = "python-cairo"
pkgver = "1.26.0"
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
sha256 = "2dddd0a874fbddb21e14acd9b955881ee1dc6e63b9c549a192d613a907f9cbeb"


@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

pkgname = "python-cairo"
pkgver = "1.24.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["pkgconf", "python-setuptools"]
makedepends = ["cairo-devel", "python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Cairo graphics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "1444d52f1bb4cc79a4a0c0fe2ccec4bd78ff885ab01ebe1c0f637d8392bcafb6"


def do_check(self):
    self.do("python", "setup.py", "test")


@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

pkgname = "python-cairo"
pkgver = "1.25.0"
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
sha256 = "37842b9bfa6339c45a5025f752e1d78d5840b1a0f82303bdd5610846ad8b5c4f"


def do_check(self):
    self.do("python", "setup.py", "test")


@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

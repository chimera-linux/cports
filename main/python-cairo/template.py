pkgname = "python-cairo"
pkgver = "1.20.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["pkgconf", "python"]
makedepends = ["cairo-devel", "python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Cairo graphics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "1ee72b035b21a475e1ed648e26541b04e5d7e753d75ca79de8c583b25785531b"

def do_check(self):
    self.do("python", "setup.py", "test")

@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

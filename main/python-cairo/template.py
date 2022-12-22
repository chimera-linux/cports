pkgname = "python-cairo"
pkgver = "1.21.0"
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
sha256 = "251907f18a552df938aa3386657ff4b5a4937dde70e11aa042bc297957f4b74b"

def do_check(self):
    self.do("python", "setup.py", "test")

@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]

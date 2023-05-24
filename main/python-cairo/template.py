pkgname = "python-cairo"
pkgver = "1.23.0"
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
sha256 = "9b61ac818723adc04367301317eb2e814a83522f07bbd1f409af0dada463c44c"


def do_check(self):
    self.do("python", "setup.py", "test")


@subpackage("python-cairo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()

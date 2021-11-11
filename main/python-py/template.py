pkgname = "python-py"
pkgver = "1.10.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools_scm"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/py"
source = f"$(PYPI_SITE)/p/py/py-{pkgver}.tar.gz"
sha256 = "21b81bda15b66ef5e1a777a21c4dcd9c20ad3efd0b3f817e7a809035269e1bd3"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

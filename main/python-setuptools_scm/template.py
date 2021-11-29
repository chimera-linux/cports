pkgname = "python-setuptools_scm"
pkgver = "6.3.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-tomli"]
depends = ["python-setuptools", "python-tomli", "python-packaging"]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools_scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "a49aa8081eeb3514eb9728fa5040f2eaa962d6c6f4ec9c32f6c1fba88f88a0f2"
# tests fail when the package is not installed
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

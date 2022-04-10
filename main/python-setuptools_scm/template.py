pkgname = "python-setuptools_scm"
pkgver = "6.4.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-tomli"]
depends = ["python-setuptools", "python-tomli", "python-packaging"]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools_scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "6833ac65c6ed9711a4d5d2266f8024cfa07c533a0e55f4c12f6eff280a5a9e30"
# tests fail when the package is not installed
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

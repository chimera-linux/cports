pkgname = "python-setuptools_scm"
pkgver = "7.0.5"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-tomli", "python-packaging"]
depends = [
    "python-setuptools", "python-tomli", "python-packaging",
    "python-typing_extensions"
]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools_scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "031e13af771d6f892b941adb6ea04545bbf91ebc5ce68c78aaf3fff6e1fb4844"
# tests fail when the package is not installed
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

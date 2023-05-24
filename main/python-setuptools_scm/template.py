pkgname = "python-setuptools_scm"
pkgver = "7.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-tomli", "python-packaging"]
depends = [
    "python",
    "python-setuptools",
    "python-tomli",
    "python-packaging",
    "python-typing_extensions",
]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools_scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "6c508345a771aad7d56ebff0e70628bf2b0ec7573762be9960214730de278f27"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

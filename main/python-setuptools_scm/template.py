pkgname = "python-setuptools_scm"
pkgver = "8.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-packaging",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-packaging",
    "python-setuptools",
]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools-scm/setuptools-scm-{pkgver}.tar.gz"
sha256 = "e69bf0b8265fdc8f4e070c98235b1b0816ffa8b7f91153400404bf68496012e3"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

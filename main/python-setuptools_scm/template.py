pkgname = "python-setuptools_scm"
pkgver = "8.0.4"
pkgrel = 2
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
    "python-typing_extensions",
]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools-scm/setuptools-scm-{pkgver}.tar.gz"
sha256 = "b5f43ff6800669595193fd09891564ee9d1d7dcb196cab4b2506d53a2e1c95c7"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

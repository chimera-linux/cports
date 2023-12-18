pkgname = "python-sphinx-removed-in"
pkgver = "0.2.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-sphinx"]
depends = ["python-sphinx"]
pkgdesc = "Sphinx extension for versionremoved and removed-in directives"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/MrSenko/sphinx-removed-in"
source = f"$(PYPI_SITE)/s/sphinx-removed-in/sphinx-removed-in-{pkgver}.tar.gz"
sha256 = "851ca7ea449d0597da548068c0fc7ca076d84483b2e873a26aa64f24cfd8cd0d"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

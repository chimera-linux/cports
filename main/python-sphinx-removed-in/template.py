pkgname = "python-sphinx-removed-in"
pkgver = "0.2.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-sphinx"]
depends = ["python-sphinx"]
pkgdesc = "Sphinx extension for versionremoved and removed-in directives"
license = "BSD-3-Clause"
url = "https://github.com/MrSenko/sphinx-removed-in"
source = f"$(PYPI_SITE)/s/sphinx-removed-in/sphinx-removed-in-{pkgver}.tar.gz"
sha256 = "a62dfeaa7962c5b6760b55de65ef3ed2ea83afa1a7c3416ac0bb7d3dec8fd2a6"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

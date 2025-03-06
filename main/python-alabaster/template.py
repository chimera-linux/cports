pkgname = "python-alabaster"
pkgver = "1.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Configurable sidebar-enabled Sphinx theme"
license = "BSD-3-Clause"
url = "https://alabaster.readthedocs.io"
source = f"$(PYPI_SITE)/a/alabaster/alabaster-{pkgver}.tar.gz"
sha256 = "c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

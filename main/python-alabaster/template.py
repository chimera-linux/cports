pkgname = "python-alabaster"
pkgver = "0.7.15"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Configurable sidebar-enabled Sphinx theme"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://alabaster.readthedocs.io"
source = f"$(PYPI_SITE)/a/alabaster/alabaster-{pkgver}.tar.gz"
sha256 = "0127f4b1db0afc914883f930e3d40763131aebac295522fc4a04d9e77c703705"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

pkgname = "python-alabaster"
pkgver = "0.7.13"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Configurable sidebar-enabled Sphinx theme"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://alabaster.readthedocs.io"
source = f"$(PYPI_SITE)/a/alabaster/alabaster-{pkgver}.tar.gz"
sha256 = "a27a4a084d5e690e16e01e03ad2b2e552c61a65469419b907243193de1a84ae2"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

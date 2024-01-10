pkgname = "python-alabaster"
pkgver = "0.7.16"
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
sha256 = "75a8b99c28a5dad50dd7f8ccdd447a121ddb3892da9e53d1ca5cca3106d58d65"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

pkgname = "python-attrs"
pkgver = "22.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"] # and other stuff, but does not matter
depends = ["python"]
pkgdesc = "Attributes without boilerplate"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://attrs.readthedocs.io"
source = f"$(PYPI_SITE)/a/attrs/attrs-{pkgver}.tar.gz"
sha256 = "29adc2665447e5191d0e7c568fde78b21f9672d344281d0c6e1ab085429b22b6"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]

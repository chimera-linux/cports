pkgname = "python-sphinxcontrib-applehelp"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Apple help book"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-applehelp/sphinxcontrib_applehelp-{pkgver}.tar.gz"
sha256 = "2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

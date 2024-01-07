pkgname = "python-sphinxcontrib-htmlhelp"
pkgver = "2.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs HTML document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp-{pkgver}.tar.gz"
sha256 = "0cbdd302815330058422b98a113195c9249825d681e18f11e8b1f78a2f11efff"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

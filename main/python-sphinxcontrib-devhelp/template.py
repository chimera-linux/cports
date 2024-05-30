pkgname = "python-sphinxcontrib-devhelp"
pkgver = "1.0.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Devhelp document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-devhelp/sphinxcontrib_devhelp-{pkgver}.tar.gz"
sha256 = "9893fd3f90506bc4b97bdb977ceb8fbd823989f4316b28c3841ec128544372d3"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

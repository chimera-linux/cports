pkgname = "python-sphinxcontrib-htmlhelp"
pkgver = "2.0.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs HTML document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-htmlhelp/sphinxcontrib_htmlhelp-{pkgver}.tar.gz"
sha256 = "c6597da06185f0e3b4dc952777a04200611ef563882e0c244d27a15ee22afa73"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

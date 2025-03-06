pkgname = "python-sphinxcontrib-htmlhelp"
pkgver = "2.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs HTML document"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-htmlhelp/sphinxcontrib_htmlhelp-{pkgver}.tar.gz"
sha256 = "c9e2916ace8aad64cc13a0d233ee22317f2b9025b9cf3295249fa985cc7082e9"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

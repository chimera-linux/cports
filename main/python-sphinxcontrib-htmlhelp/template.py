pkgname = "python-sphinxcontrib-htmlhelp"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs HTML document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp-{pkgver}.tar.gz"
sha256 = "f5f8bb2d0d629f398bf47d0d69c07bc13b65f75a81ad9e2f71a63d4b7a2f6db2"
# circular checkdepends
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")

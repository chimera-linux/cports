pkgname = "python-sphinxcontrib-applehelp"
pkgver = "1.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Apple help book"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-applehelp/sphinxcontrib_applehelp-{pkgver}.tar.gz"
sha256 = "c40a4f96f3776c4393d933412053962fac2b84f4c99a7982ba42e09576a70619"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

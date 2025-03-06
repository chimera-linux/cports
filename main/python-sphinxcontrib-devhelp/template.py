pkgname = "python-sphinxcontrib-devhelp"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Devhelp document"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-devhelp/sphinxcontrib_devhelp-{pkgver}.tar.gz"
sha256 = "411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

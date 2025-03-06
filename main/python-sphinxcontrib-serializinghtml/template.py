pkgname = "python-sphinxcontrib-serializinghtml"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs serialized HTML document"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-serializinghtml/sphinxcontrib_serializinghtml-{pkgver}.tar.gz"
sha256 = "e9d912827f872c029017a53f0ef2180b327c3f7fd23c87229f7a8e8b70031d4d"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

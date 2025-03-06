pkgname = "python-sphinxcontrib-qthelp"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs QtHelp document"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = (
    f"$(PYPI_SITE)/s/sphinxcontrib-qthelp/sphinxcontrib_qthelp-{pkgver}.tar.gz"
)
sha256 = "4fe7d0ac8fc171045be623aba3e2a8f613f8682731f9153bb2e40ece16b9bbab"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

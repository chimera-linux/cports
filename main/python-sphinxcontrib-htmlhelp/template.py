pkgname = "python-sphinxcontrib-htmlhelp"
pkgver = "2.0.5"
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
sha256 = "0dc87637d5de53dd5eec3a6a01753b1ccf99494bd756aafecd74b4fa9e729015"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

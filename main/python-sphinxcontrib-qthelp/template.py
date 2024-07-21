pkgname = "python-sphinxcontrib-qthelp"
pkgver = "1.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs QtHelp document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = (
    f"$(PYPI_SITE)/s/sphinxcontrib-qthelp/sphinxcontrib_qthelp-{pkgver}.tar.gz"
)
sha256 = "db3f8fa10789c7a8e76d173c23364bdf0ebcd9449969a9e6a3dd31b8b7469f03"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

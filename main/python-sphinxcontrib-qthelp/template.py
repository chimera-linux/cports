pkgname = "python-sphinxcontrib-qthelp"
pkgver = "1.0.7"
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
sha256 = "053dedc38823a80a7209a80860b16b722e9e0209e32fea98c90e4e6624588ed6"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

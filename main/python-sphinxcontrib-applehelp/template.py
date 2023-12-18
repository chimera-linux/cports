pkgname = "python-sphinxcontrib-applehelp"
pkgver = "1.0.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Apple help book"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-applehelp/sphinxcontrib-applehelp-{pkgver}.tar.gz"
sha256 = "828f867945bbe39817c210a1abfd1bc4895c8b73fcaade56d45357a348a07d7e"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

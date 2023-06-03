pkgname = "python-markupsafe"
pkgver = "2.1.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "XML/HTML/XHTML Markup safe string for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/markupsafe"
source = f"$(PYPI_SITE)/M/MarkupSafe/MarkupSafe-{pkgver}.tar.gz"
sha256 = "af598ed32d6ae86f1b747b82783958b1a4ab8f617b06fe68795c7f026abbdcad"
# dependency of pytest; also needs itsself to be installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

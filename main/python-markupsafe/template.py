pkgname = "python-markupsafe"
pkgver = "2.1.2"
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
sha256 = "abcabc8c2b26036d62d4c746381a6f7cf60aafcc653198ad678306986b09450d"
# dependency of pytest; also needs itsself to be installed
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.rst")

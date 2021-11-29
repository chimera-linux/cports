pkgname = "python-markupsafe"
pkgver = "2.0.1"
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
sha256 = "594c67807fb16238b30c44bdf74f36c02cdf22d1c8cda91ef8a0ed8dabf5620a"
# dependency of pytest; also needs itsself to be installed
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.rst")

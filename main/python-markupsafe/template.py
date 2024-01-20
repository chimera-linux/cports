pkgname = "python-markupsafe"
pkgver = "2.1.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "XML/HTML/XHTML Markup safe string for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/markupsafe"
source = f"$(PYPI_SITE)/M/MarkupSafe/MarkupSafe-{pkgver}.tar.gz"
sha256 = "3aae9af4cac263007fd6309c64c6ab4506dd2b79382d9d19a1994f9240b8db4f"
# dependency of pytest; also needs itsself to be installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

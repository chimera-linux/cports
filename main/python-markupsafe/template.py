pkgname = "python-markupsafe"
pkgver = "3.0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "XML/HTML/XHTML Markup safe string for Python"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/markupsafe"
source = f"$(PYPI_SITE)/M/MarkupSafe/markupsafe-{pkgver}.tar.gz"
sha256 = "722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698"
# dependency of pytest; also needs itself to be installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

pkgname = "python-ujson"
pkgver = "5.10.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Native json encoder for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause AND TCL"
url = "https://github.com/ultrajson/ultrajson"
source = f"$(PYPI_SITE)/u/ujson/ujson-{pkgver}.tar.gz"
sha256 = "b3cd8f3c5d8c7738257f1018880444f7b7d9b66232c64649f562d7ba86ad4bc1"


def post_install(self):
    self.install_license("LICENSE.txt")

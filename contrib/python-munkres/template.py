pkgname = "python-munkres"
pkgver = "1.1.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Algorithm for the Assignment Problem in Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "Apache-2.0"
url = "http://software.clapper.org/munkres"
source = f"$(PYPI_SITE)/m/munkres/munkres-{pkgver}.tar.gz"
sha256 = "fc44bf3c3979dada4b6b633ddeeb8ffbe8388ee9409e4d4e8310c2da1792db03"


def post_install(self):
    self.install_license("LICENSE.md")

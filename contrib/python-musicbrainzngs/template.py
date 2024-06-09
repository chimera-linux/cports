pkgname = "python-musicbrainzngs"
pkgver = "0.7.1"
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
pkgdesc = "Musicbrainz NGS webservice interface python bindings"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "BSD-2-Clause"
url = "https://github.com/alastair/python-musicbrainzngs"
source = f"$(PYPI_SITE)/m/musicbrainzngs/musicbrainzngs-{pkgver}.tar.gz"
sha256 = "ab1c0100fd0b305852e65f2ed4113c6de12e68afd55186987b8ed97e0f98e627"


def post_install(self):
    self.install_license("COPYING")

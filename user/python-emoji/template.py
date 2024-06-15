pkgname = "python-emoji"
pkgver = "2.14.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for emoji support"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/carpedm20/emoji"
source = f"$(PYPI_SITE)/e/emoji/emoji-{pkgver}.tar.gz"
sha256 = "f8c50043d79a2c1410ebfae833ae1868d5941a67a6cd4d18377e2eb0bd79346b"


def post_install(self):
    self.install_license("LICENSE.txt")

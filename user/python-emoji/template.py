pkgname = "python-emoji"
pkgver = "2.15.0"
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
license = "BSD-3-Clause"
url = "https://github.com/carpedm20/emoji"
source = f"$(PYPI_SITE)/e/emoji/emoji-{pkgver}.tar.gz"
sha256 = "eae4ab7d86456a70a00a985125a03263a5eac54cd55e51d7e184b1ed3b6757e4"


def post_install(self):
    self.install_license("LICENSE.txt")

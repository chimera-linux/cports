pkgname = "python-unidecode"
pkgver = "1.3.8"
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
pkgdesc = "ASCII transliterations of Unicode text for Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "GPL-2.0-or-later"
url = "https://pypi.org/project/Unidecode"
source = f"$(PYPI_SITE)/U/Unidecode/Unidecode-{pkgver}.tar.gz"
sha256 = "cfdb349d46ed3873ece4586b96aa75258726e2fa8ec21d6f00a591d98806c2f4"


def post_install(self):
    self.install_license("LICENSE")

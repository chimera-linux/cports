pkgname = "python-pysol_cards"
pkgver = "0.24.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for dealing cards like various solitaire games"
license = "MIT"
url = "https://github.com/shlomif/pysol_cards"
source = f"$(PYPI_SITE)/p/pysol_cards/pysol_cards-{pkgver}.tar.gz"
sha256 = "a985492da81aa1588dfc056d9a7c6ca83f66254c0b90f25afc682a70713d4d4b"


def post_install(self):
    self.install_license("LICENSE")

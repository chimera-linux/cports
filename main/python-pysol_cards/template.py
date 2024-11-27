pkgname = "python-pysol_cards"
pkgver = "0.18.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shlomif/pysol_cards"
source = f"$(PYPI_SITE)/p/pysol_cards/pysol_cards-{pkgver}.tar.gz"
sha256 = "29196eadd51a54a7bf853d0aecba168853903a24803b8554713e8c7fcc732c2c"


def post_install(self):
    self.install_license("LICENSE")

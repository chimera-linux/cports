pkgname = "python-pysol_cards"
pkgver = "0.16.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-random2",
    "python-six",
]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python module for dealing cards like various solitaire games"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/shlomif/pysol_cards"
source = f"$(PYPI_SITE)/p/pysol_cards/pysol_cards-{pkgver}.tar.gz"
sha256 = "0b87ca7b3f99155cccd3cfd739f739f7744d6f8198222c6d493a034a3d4570c3"


def post_install(self):
    self.install_license("LICENSE")

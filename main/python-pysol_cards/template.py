pkgname = "python-pysol_cards"
pkgver = "0.22.0"
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
sha256 = "c555ef5e05ad41774e742b603ce6e6ba76e5d013ddf4ae087a3d87c55279f142"


def post_install(self):
    self.install_license("LICENSE")

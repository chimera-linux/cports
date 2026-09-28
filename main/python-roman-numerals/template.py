pkgname = "python-roman-numerals"
pkgver = "4.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
renames = ["python-roman-numerals-py"]
pkgdesc = "Manipulate Roman numerals"
license = "0BSD OR CC0-1.0"
url = "https://github.com/AA-Turner/roman-numerals"
source = f"$(PYPI_SITE)/r/roman-numerals/roman_numerals-{pkgver}.tar.gz"
sha256 = "1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2"
# cyclic
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

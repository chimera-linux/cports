pkgname = "python-roman-numerals-py"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Manipulate Roman numerals"
license = "0BSD OR CC0-1.0"
url = "https://github.com/AA-Turner/roman-numerals"
source = f"$(PYPI_SITE)/r/roman-numerals-py/roman_numerals_py-{pkgver}.tar.gz"
sha256 = "be4bf804f083a4ce001b5eb7e3c0862479d10f94c936f6c4e5f250aa5ff5bd2d"
# cyclic
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.rst")

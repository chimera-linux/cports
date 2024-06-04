pkgname = "python-jaraco.classes"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-more-itertools"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Utility functions for Python class constructs"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/jaraco.classes"
source = f"$(PYPI_SITE)/j/jaraco.classes/jaraco.classes-{pkgver}.tar.gz"
sha256 = "47a024b51d0239c0dd8c8540c6c7f484be3b8fcf0b2d85c13825780d3b3f3acd"


def post_install(self):
    self.install_license("LICENSE")

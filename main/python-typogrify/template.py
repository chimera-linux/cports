pkgname = "python-typogrify"
pkgver = "2.0.7"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-smartypants"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Filters to enhance web typography"
license = "BSD-3-Clause"
url = "https://github.com/mintchaos/typogrify"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d5081966c1c1423157e240d5cfe7435b56ca30be57ff8c7fe6f90f6cc42295ee"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

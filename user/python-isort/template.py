pkgname = "python-isort"
pkgver = "6.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-colorama",
    "python-setuptools",
]
checkdepends = [
    *depends,
    "python-pytest",
    "python-hypothesis",
    "python-black",
]
pkgdesc = "Python library for sorting imports"
license = "MIT"
url = "https://pycqa.github.io/isort"
source = f"$(PYPI_SITE)/i/isort/isort-{pkgver}.tar.gz"
sha256 = "1cb5df28dfbc742e490c5e41bad6da41b805b0a8be7bc93cd0fb2a8a890ac450"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

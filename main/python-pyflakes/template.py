pkgname = "python-pyflakes"
pkgver = "3.3.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python code linter"
license = "MIT"
url = "https://github.com/PyCQA/pyflakes"
source = f"$(PYPI_SITE)/p/pyflakes/pyflakes-{pkgver}.tar.gz"
sha256 = "6dfd61d87b97fba5dcfaaf781171ac16be16453be6d816147989e7f6e6a9576b"


def post_install(self):
    self.install_license("LICENSE")

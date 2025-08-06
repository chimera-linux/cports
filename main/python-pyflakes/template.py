pkgname = "python-pyflakes"
pkgver = "3.4.0"
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
sha256 = "b24f96fafb7d2ab0ec5075b7350b3d2d2218eab42003821c06344973d3ea2f58"


def post_install(self):
    self.install_license("LICENSE")

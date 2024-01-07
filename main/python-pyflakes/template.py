pkgname = "python-pyflakes"
pkgver = "3.2.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pyflakes"
source = f"$(PYPI_SITE)/p/pyflakes/pyflakes-{pkgver}.tar.gz"
sha256 = "1c61603ff154621fb2a9172037d84dca3500def8c8b630657d1701f026f8af3f"


def post_install(self):
    self.install_license("LICENSE")

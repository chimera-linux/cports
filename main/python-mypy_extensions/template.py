pkgname = "python-mypy_extensions"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests/testextensions.py"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Extensions for Python typing module"
license = "MIT"
url = "https://github.com/python/mypy_extensions"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "178030dd39335042c2c5becccc596c2f307f796868f9c627da3fe14d76de9d97"


def post_install(self):
    self.install_license("LICENSE")

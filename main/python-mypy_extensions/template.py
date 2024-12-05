pkgname = "python-mypy_extensions"
pkgver = "1.0.0"
pkgrel = 2
build_style = "python_pep517"
make_check_target = "tests/testextensions.py"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Extensions for Python typing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python/mypy_extensions"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c1f1fc0cc5f5be7d3a70b6dd4b85f9e2b02d788d66f3a168652a65df6571df07"


def post_install(self):
    self.install_license("LICENSE")

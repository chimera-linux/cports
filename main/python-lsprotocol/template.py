pkgname = "python-lsprotocol"
pkgver = "2025.0.0"
pkgrel = 0
build_wrksrc = "packages/python"
build_style = "python_pep517"
make_check_args = ["../../tests/python"]
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = [
    "python-attrs",
    "python-cattrs",
    "python-jsonschema",
]
checkdepends = [
    "python-pyhamcrest",
    "python-pytest",
    *depends,
]
pkgdesc = "Language server protocol types for Python"
license = "MIT"
url = "https://github.com/microsoft/lsprotocol"
# no tests in pypi
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f5e93c080c01ac27896114b996929e8474943b189b2a2dbf304dcd4663596d5c"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "python-lsprotocol"
pkgver = "2023.0.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/microsoft/lsprotocol"
# no tests in pypi
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0697ef66ca1b547cadb4c27080d6095c2e403b9aeb05401de383126a70720a56"


def post_install(self):
    self.install_license("LICENSE")

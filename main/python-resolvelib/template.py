pkgname = "python-resolvelib"
pkgver = "1.2.1"
pkgrel = 0
build_style = "python_pep517"
# version mismatches
make_check_args = [
    "--deselect",
    "tests/functional/python/test_resolvers_python.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-commentjson", "python-packaging", "python-pytest"]
depends = ["python"]
pkgdesc = "Resolve abstract dependencies into concrete ones"
license = "ISC"
url = "https://github.com/sarugaku/resolvelib"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4d4c4137d7b8f8f27f298ff1af2faa767d790f271928506358d25e4252ed749a"


def post_install(self):
    self.install_license("LICENSE")

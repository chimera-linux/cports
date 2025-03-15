pkgname = "python-pyproject-metadata"
pkgver = "0.9.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["python-packaging"]
pkgdesc = "PEP 621 metadata parsing"
license = "MIT"
url = "https://github.com/pypa/pyproject-metadata"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "95213045cf74cb32642034ccb4b3223c2a4337fa675fa886cbd48be6780241c7"


def post_install(self):
    self.install_license("LICENSE")

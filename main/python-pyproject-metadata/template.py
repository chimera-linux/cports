pkgname = "python-pyproject-metadata"
pkgver = "0.10.0"
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
sha256 = "f0e5d416d0851b89198cb112ff568adbb75da7d4941ca23f5a16690163785277"


def post_install(self):
    self.install_license("LICENSE")

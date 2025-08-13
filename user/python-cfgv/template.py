pkgname = "python-cfgv"
pkgver = "3.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Schema-based configuration validator"
license = "MIT"
url = "https://github.com/asottile/cfgv"
# pypi does not have tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "13d7bd4125dd3deed477cbfad9e8fb44a442f0bb627b5cd03afb6bc1899538db"


def post_install(self):
    self.install_license("LICENSE")

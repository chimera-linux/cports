pkgname = "python-spinners"
pkgver = "0.0.24"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "More than 60 spinners for terminal"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "MIT"
url = "https://github.com/manrajgrover/py-spinners"
source = f"{url}/archive/a73d561aa58b12afc3aa4ee80143dca87656688d.zip"
sha256 = "e45e6e00b711e75ec6d6e5b0970cd099c0b9c3e340aa1edbe24eef04a0053393"


def post_install(self):
    self.install_license("LICENSE")

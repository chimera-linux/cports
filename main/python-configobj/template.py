pkgname = "python-configobj"
pkgver = "5.0.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python config file reader and writer"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/DiffSK/configobj"
source = f"https://github.com/DiffSK/configobj/archive/v{pkgver}.tar.gz"
sha256 = "2bd70f9ce7912679c4ba9c80da289877906db0ca6bd02c3ab545d660e9b60d4f"


def post_install(self):
    self.install_license("LICENSE")

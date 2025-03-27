pkgname = "python-flexparser"
pkgver = "0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python parsing library using typing"
license = "BSD-3-Clause"
url = "https://github.com/hgrecco/flexparser"
source = f"$(PYPI_SITE)/f/flexparser/flexparser-{pkgver}.tar.gz"
sha256 = "266d98905595be2ccc5da964fe0a2c3526fbbffdc45b65b3146d75db992ef6b2"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "python-constantly"
pkgver = "23.10.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-versioneer",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Symbolic constants for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/twisted/constantly"
source = f"$(PYPI_SITE)/c/constantly/constantly-{pkgver}.tar.gz"
sha256 = "aa92b70a33e2ac0bb33cd745eb61776594dc48764b06c35e0efd050b7f1c7cbd"
# circular with python-twisted
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

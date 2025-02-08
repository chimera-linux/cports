pkgname = "python-portend"
pkgver = "3.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-tempora"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "TCP port monitoring and discovery"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/portend"
source = f"$(PYPI_SITE)/p/portend/portend-{pkgver}.tar.gz"
sha256 = "5250a352c19c959d767cac878b829d93e5dc7625a5143399a2a00dc6628ffb72"


def post_install(self):
    self.install_license("LICENSE")

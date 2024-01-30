pkgname = "python-patatt"
pkgver = "0.6.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pynacl"]
pkgdesc = (
    "Library that adds cryptographic attestation to patches sent via email"
)
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT-0"
url = "https://git.kernel.org/pub/scm/utils/patatt/patatt.git"
source = f"$(PYPI_SITE)/p/patatt/patatt-{pkgver}.tar.gz"
sha256 = "980826f6529d2576c267ca1f564d5bef046cb47e54215bb598ed6c4b9b2d0a28"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")

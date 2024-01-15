pkgname = "python-itsdangerous"
pkgver = "2.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
pkgdesc = "Python3 helper to pass trusted data to untrusted environments"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "BSD-3-Clause"
url = "https://github.com/pallets/itsdangerous"
source = f"$(PYPI_SITE)/i/itsdangerous/itsdangerous-{pkgver}.tar.gz"
sha256 = "5dbbc68b317e5e42f327f9021763545dc3fc3bfe22e6deb96aaf1fc38874156a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

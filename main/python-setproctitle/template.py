pkgname = "python-setproctitle"
pkgver = "1.3.6"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for process title customization"
license = "BSD-3-Clause"
url = "https://github.com/dvarrazzo/py-setproctitle"
source = f"$(PYPI_SITE)/s/setproctitle/setproctitle-{pkgver}.tar.gz"
sha256 = "c9f32b96c700bb384f33f7cf07954bb609d35dd82752cef57fb2ee0968409169"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")

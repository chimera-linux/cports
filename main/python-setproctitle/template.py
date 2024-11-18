pkgname = "python-setproctitle"
pkgver = "1.3.4"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for process title customization"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/dvarrazzo/py-setproctitle"
source = f"$(PYPI_SITE)/s/setproctitle/setproctitle-{pkgver}.tar.gz"
sha256 = "3b40d32a3e1f04e94231ed6dfee0da9e43b4f9c6b5450d53e6dd7754c34e0c50"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")

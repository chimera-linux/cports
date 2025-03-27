pkgname = "python-setproctitle"
pkgver = "1.3.5"
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
license = "BSD-3-Clause"
url = "https://github.com/dvarrazzo/py-setproctitle"
source = f"$(PYPI_SITE)/s/setproctitle/setproctitle-{pkgver}.tar.gz"
sha256 = "1e6eaeaf8a734d428a95d8c104643b39af7d247d604f40a7bebcf3960a853c5e"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")

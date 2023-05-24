pkgname = "python-setproctitle"
pkgver = "1.3.2"
pkgrel = 0
build_style = "python_module"
make_check_target = "tests"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for process title customization"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/dvarrazzo/py-setproctitle"
source = f"$(PYPI_SITE)/s/setproctitle/setproctitle-{pkgver}.tar.gz"
sha256 = "b9fb97907c830d260fa0658ed58afd48a86b2b88aac521135c352ff7fd3477fd"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")

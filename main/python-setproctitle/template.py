pkgname = "python-setproctitle"
pkgver = "1.3.3"
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
sha256 = "c913e151e7ea01567837ff037a23ca8740192880198b7fbb90b16d181607caae"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")

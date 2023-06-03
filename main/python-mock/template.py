pkgname = "python-mock"
pkgver = "5.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python mock library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://mock.readthedocs.org"
source = f"$(PYPI_SITE)/m/mock/mock-{pkgver}.tar.gz"
sha256 = "06f18d7d65b44428202b145a9a36e99c2ee00d1eb992df0caf881d4664377891"


def post_install(self):
    self.install_license("LICENSE.txt")

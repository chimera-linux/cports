pkgname = "python-parameterized"
pkgver = "0.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Parameterized testing with any Python test framework"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/wolever/parameterized"
source = f"$(PYPI_SITE)/p/parameterized/parameterized-{pkgver}.tar.gz"
sha256 = "7fc905272cefa4f364c1a3429cbbe9c0f98b793988efb5bf90aac80f08db09b1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

pkgname = "python-dill"
pkgver = "0.3.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python serialization library"
license = "BSD-3-Clause"
url = "https://github.com/uqfoundation/dill"
source = f"$(PYPI_SITE)/d/dill/dill-{pkgver}.tar.gz"
sha256 = "81aa267dddf68cbfe8029c42ca9ec6a4ab3b22371d1c450abc54422577b4512c"
# broken test module import
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

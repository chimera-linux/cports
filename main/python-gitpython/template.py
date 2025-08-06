pkgname = "python-gitpython"
pkgver = "3.1.45"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-gitdb"]
pkgdesc = "Python library to interact with Git repos"
license = "BSD-3-Clause"
url = "https://gitpython.readthedocs.org"
source = f"$(PYPI_SITE)/g/GitPython/gitpython-{pkgver}.tar.gz"
sha256 = "85b0ee964ceddf211c41b9f27a49086010a190fd8132a24e21f362a4b36a791c"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

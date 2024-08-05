pkgname = "python-gitpython"
pkgver = "3.1.43"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-gitdb"]
pkgdesc = "Python library to interact with Git repos"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://gitpython.readthedocs.org"
source = f"$(PYPI_SITE)/g/GitPython/GitPython-{pkgver}.tar.gz"
sha256 = "35f314a9f878467f5453cc1fee295c3e18e52f1b99f10f6cf5b1682e968a9e7c"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

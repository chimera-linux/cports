pkgname = "python-gitpython"
pkgver = "3.1.44"
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
source = f"$(PYPI_SITE)/g/GitPython/gitpython-{pkgver}.tar.gz"
sha256 = "c87e30b26253bf5418b01b0660f818967f3c503193838337fe5e573331249269"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

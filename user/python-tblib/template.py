pkgname = "python-tblib"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
    "python-twisted",
]
pkgdesc = "Traceback serialization library"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/python-tblib"
source = f"$(PYPI_SITE)/t/tblib/tblib-{pkgver}.tar.gz"
sha256 = "06404c2c9f07f66fee2d7d6ad43accc46f9c3361714d9b8426e7f47e595cd652"
# FIXME: failing tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

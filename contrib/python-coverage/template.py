pkgname = "python-coverage"
pkgver = "7.5.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-flaky",
    "python-hypothesis",
    "python-pytest",
    "python-pytest-xdist",
]
pkgdesc = "Code coverage tool for Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "Apache-2.0"
url = "https://coverage.readthedocs.io"
source = f"$(PYPI_SITE)/c/coverage/coverage-{pkgver}.tar.gz"
sha256 = "04aefca5190d1dc7a53a4c1a5a7f8568811306d7a8ee231c42fb69215571944f"
# Some failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

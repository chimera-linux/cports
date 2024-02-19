pkgname = "python-dnspython"
pkgver = "2.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "DNS toolkit for Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "ISC"
url = "https://www.dnspython.org"
source = f"$(PYPI_SITE)/d/dnspython/dnspython-{pkgver}.tar.gz"
sha256 = "e8f0f9c23a7b7cb99ded64e6c3a6f3e701d78f50c55e002b839dea7225cff7cc"


def post_install(self):
    self.install_license("LICENSE")

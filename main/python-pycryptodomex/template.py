pkgname = "python-pycryptodomex"
pkgver = "3.20.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Self-contained cryptographic library for Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSD-2-Clause AND Unlicense"
url = "https://www.pycryptodome.org"
source = f"$(PYPI_SITE)/p/pycryptodomex/pycryptodomex-{pkgver}.tar.gz"
sha256 = "7a710b79baddd65b806402e14766c721aee8fb83381769c27920f26476276c1e"
# FIXME: doesn't seem to be able to load its own libraries?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

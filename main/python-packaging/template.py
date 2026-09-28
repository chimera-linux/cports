pkgname = "python-packaging"
pkgver = "26.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-installer", "python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python", "python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"
# needs pytest, is a dependency of pytest
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")

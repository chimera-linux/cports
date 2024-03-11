pkgname = "python-packaging"
pkgver = "24.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-installer", "python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python", "python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "eb82c5e3e56209074766e6885bb04b8c38a0c015d0a30036ebe7ece34c9989e9"
# needs pytest, is a dependency of pytest
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")

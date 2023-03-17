pkgname = "python-packaging"
pkgver = "23.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-pip", "python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python", "python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "b6ad297f8907de0fa2fe1ccbd26fdaf387f5f47c7275fedf8cce89f99446cf97"
# needs pytest, is a dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

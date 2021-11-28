pkgname = "python-packaging"
pkgver = "21.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "dd47c42927d89ab911e606518907cc2d3a1f38bbd026385970643f9c5b8ecfeb"
# needs pytest, is a dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")

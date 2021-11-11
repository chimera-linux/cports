pkgname = "python-packaging"
pkgver = "21.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "096d689d78ca690e4cd8a89568ba06d07ca097e3306a4381635073ca91479966"
# needs pytest, is a dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

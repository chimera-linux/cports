pkgname = "python-pluggy"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools_scm"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Minimalist production ready plugin system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pluggy"
source = f"$(PYPI_SITE)/p/pluggy/pluggy-{pkgver}.tar.gz"
sha256 = "c500b592c5512df35622e4faf2135aa0b7e989c7d31344194b4afb9d5e47b1bf"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

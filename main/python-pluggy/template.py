pkgname = "python-pluggy"
pkgver = "1.2.0"
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
sha256 = "d12f0c4b579b15f5e054301bb226ee85eeeba08ffec228092f8defbaa3a4c4b3"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

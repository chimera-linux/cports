pkgname = "python-pluggy"
pkgver = "1.3.0"
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
sha256 = "cf61ae8f126ac6f7c451172cf30e3e43d3ca77615509771b3a984a0730651e12"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

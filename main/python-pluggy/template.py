pkgname = "python-pluggy"
pkgver = "0.13.1"
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
sha256 = "15b2acde666561e1298d71b523007ed7364de07029219b604cf808bfa1c765b0"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

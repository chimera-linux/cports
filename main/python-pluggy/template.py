pkgname = "python-pluggy"
pkgver = "1.0.0"
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
sha256 = "4224373bacce55f955a878bf9cfa763c1e360858e330072059e10bad68531159"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

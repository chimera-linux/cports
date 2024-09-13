pkgname = "python-platformdirs"
pkgver = "4.3.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest", "python-appdirs", "python-pytest-mock"]
depends = ["python"]
pkgdesc = "Platform-specific system directory library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://platformdirs.readthedocs.io"
source = f"$(PYPI_SITE)/p/platformdirs/platformdirs-{pkgver}.tar.gz"
sha256 = "d4e0b7d8ec176b341fb03cb11ca12d0276faa8c485f9cd218f613840463fc2c0"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

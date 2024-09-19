pkgname = "python-platformdirs"
pkgver = "4.3.6"
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
sha256 = "357fb2acbc885b0419afd3ce3ed34564c13c9b95c89360cd9563f73aa5e2b907"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

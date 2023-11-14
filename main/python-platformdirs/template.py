pkgname = "python-platformdirs"
pkgver = "4.0.0"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest", "python-appdirs", "python-pytest-mock"]
depends = ["python"]
pkgdesc = "Platform-specific system directory library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://platformdirs.readthedocs.io"
source = f"$(PYPI_SITE)/p/platformdirs/platformdirs-{pkgver}.tar.gz"
sha256 = "cb633b2bcf10c51af60beb0ab06d2f1d69064b43abf4c185ca6b28865f3f9731"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

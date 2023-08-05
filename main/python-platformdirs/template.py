pkgname = "python-platformdirs"
pkgver = "3.10.0"
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
sha256 = "b45696dab2d7cc691a3226759c0d3b00c47c8b6e293d96f6436f733303f77f6d"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

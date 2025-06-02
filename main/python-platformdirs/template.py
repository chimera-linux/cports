pkgname = "python-platformdirs"
pkgver = "4.3.8"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest", "python-appdirs", "python-pytest-mock"]
depends = ["python"]
pkgdesc = "Platform-specific system directory library"
license = "MIT"
url = "https://platformdirs.readthedocs.io"
source = f"$(PYPI_SITE)/p/platformdirs/platformdirs-{pkgver}.tar.gz"
sha256 = "3d512d96e16bcb959a814c9f348431070822a6496326a4be0911c40b5a74c2bc"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

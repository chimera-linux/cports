pkgname = "python-py"
pkgver = "1.11.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python development support library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/py"
source = f"$(PYPI_SITE)/p/py/py-{pkgver}.tar.gz"
sha256 = "51c75c4126074b472f746a24399ad32f6053d1b34b68d2fa41e558e6f4a98719"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

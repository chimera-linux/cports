pkgname = "python-pluggy"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Minimalist production ready plugin system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pluggy"
source = f"$(PYPI_SITE)/p/pluggy/pluggy-{pkgver}.tar.gz"
sha256 = "2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

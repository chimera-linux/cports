pkgname = "python-pluggy"
pkgver = "1.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Minimalist production ready plugin system"
license = "MIT"
url = "https://github.com/pytest-dev/pluggy"
source = f"$(PYPI_SITE)/p/pluggy/pluggy-{pkgver}.tar.gz"
sha256 = "7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

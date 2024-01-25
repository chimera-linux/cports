pkgname = "python-pluggy"
pkgver = "1.4.0"
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
sha256 = "8c85c2876142a764e5b7548e7d9a0e0ddb46f5185161049a79b7e974454223be"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

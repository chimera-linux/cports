pkgname = "python-six"
pkgver = "1.16.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python compatibility utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/benjaminp/six"
source = f"$(PYPI_SITE)/s/six/six-{pkgver}.tar.gz"
sha256 = "1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"
# dependency of core stuff
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

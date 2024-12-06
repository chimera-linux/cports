pkgname = "python-six"
pkgver = "1.17.0"
pkgrel = 0
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
sha256 = "ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81"
# dependency of core stuff
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

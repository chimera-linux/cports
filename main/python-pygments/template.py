pkgname = "python-pygments"
pkgver = "2.17.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/p/pygments/pygments-{pkgver}.tar.gz"
sha256 = "da46cec9fd2de5be3a8a784f434e4c4ab670b4ff54d605c4c2717e9d49c4c367"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

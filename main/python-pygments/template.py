pkgname = "python-pygments"
pkgver = "2.19.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/p/pygments/pygments-{pkgver}.tar.gz"
sha256 = "636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

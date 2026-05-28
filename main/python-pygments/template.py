pkgname = "python-pygments"
pkgver = "2.20.0"
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
sha256 = "6757cd03768053ff99f3039c1a36d6c0aa0b263438fcab17520b30a303a82b5f"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

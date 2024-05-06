pkgname = "python-pygments"
pkgver = "2.18.0"
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
sha256 = "786ff802f32e91311bff3889f6e9a86e81505fe99f2735bb6d60ae0c5004f199"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

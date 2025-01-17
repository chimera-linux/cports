pkgname = "python-pygments"
pkgver = "2.19.1"
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
sha256 = "61c16d2a8576dc0649d9f39e089b5f02bcd27fba10d8fb4dcc28173f7a45151f"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

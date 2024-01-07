pkgname = "python-pygments"
pkgver = "2.16.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "1daff0494820c69bc8941e407aa20f577374ee88364ee10a98fdbe0aece96e29"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

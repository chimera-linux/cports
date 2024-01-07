pkgname = "python-snowballstemmer"
pkgver = "2.2.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Snowball stemming library collection for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/shibukawa/snowball_py"
source = f"$(PYPI_SITE)/s/snowballstemmer/snowballstemmer-{pkgver}.tar.gz"
sha256 = "09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")

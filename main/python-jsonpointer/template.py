pkgname = "python-jsonpointer"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Identify specific nodes in a JSON document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/stefankoegl/python-json-pointer"
source = f"$(PYPI_SITE)/j/jsonpointer/jsonpointer-{pkgver}.tar.gz"
sha256 = "2b2d729f2091522d61c3b31f82e11870f60b68f43fbc705cb76bf4b832af59ef"
# does not use pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

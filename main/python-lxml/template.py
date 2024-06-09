pkgname = "python-lxml"
pkgver = "5.2.2"
pkgrel = 1
build_style = "python_pep517"
make_build_env = {"WITH_CYTHON": "true"}
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["libxslt-devel", "libxml2-devel", "python-devel"]
depends = ["python"]
pkgdesc = "Python bindings for the libxml2 and libxslt libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND custom:ElementTree"
url = "https://lxml.de"
source = f"https://github.com/lxml/lxml/archive/lxml-{pkgver}.tar.gz"
sha256 = "1801c8576a4fca14d46561f2963cebe4dad2c90f6d98aaaa4f241eff757e7c6c"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

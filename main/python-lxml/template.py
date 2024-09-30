pkgname = "python-lxml"
pkgver = "5.3.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"WITH_CYTHON": "true"}
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = ["libxslt-devel", "libxml2-devel", "python-devel"]
depends = ["python"]
checkdepends = ["python-html5lib"]
pkgdesc = "Python bindings for the libxml2 and libxslt libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND custom:ElementTree"
url = "https://lxml.de"
source = f"https://github.com/lxml/lxml/archive/lxml-{pkgver}.tar.gz"
sha256 = "eb22f7ceb319c29247cfa398435d00e6286d19a32b4870b67a8e9a38d72f2ebd"
patch_style = "patch"


def check(self):
    self.do("make", "test")


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

pkgname = "python-lxml"
pkgver = "5.3.1"
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
sha256 = "db2ec01227b01888b6d5458fc1ade6e6bbf3cdc52a63c3b072378851b81e59f1"


def check(self):
    self.do("make", "test")


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

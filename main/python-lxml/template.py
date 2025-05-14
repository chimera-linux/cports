pkgname = "python-lxml"
pkgver = "5.4.0"
pkgrel = 1
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
license = "BSD-3-Clause AND custom:ElementTree"
url = "https://lxml.de"
source = f"https://github.com/lxml/lxml/archive/lxml-{pkgver}.tar.gz"
sha256 = "12ed971a99bd07977e236bf59314cfd53fbf5d59f39d4a13caad901c7fceb0a2"


def post_extract(self):
    # not supported by libxml2 anymore
    self.rm("src/lxml/tests/test_http_io.py")


def check(self):
    self.do("make", "test")


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

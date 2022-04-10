pkgname = "python-lxml"
pkgver = "4.8.0"
pkgrel = 0
build_style = "python_module"
make_build_args = ["--with-cython"]
hostmakedepends = ["python-cython", "python-setuptools"]
makedepends = ["libxslt-devel", "libxml2-devel", "python-devel"]
pkgdesc = "Python bindings for the libxml2 and libxslt libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND custom:ElementTree"
url = "https://lxml.de"
source = f"https://github.com/lxml/lxml/archive/lxml-{pkgver}.tar.gz"
sha256 = "8d2b999f5c8a8a70a28a3875e5d1bf27c0555c922bfa0af34dc46e07913f2a47"
# missing checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

pkgname = "python-lxml"
pkgver = "4.9.3"
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
sha256 = "42b9ab83cb8739d817c7fff41c20f31aa61625bb6f6ab333873a5f3406b139ac"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

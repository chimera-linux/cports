pkgname = "python-lxml"
pkgver = "4.6.4"
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
sha256 = "5a7cef132353fc36de6f6b26dacde07b22217c6b4f8c11ef48e8bf0011f48160"
# missing checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

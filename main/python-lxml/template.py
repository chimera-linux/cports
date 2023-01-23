pkgname = "python-lxml"
pkgver = "4.9.1"
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
sha256 = "e46a74cef580e069586b7a98e9a74b49e56b849822130654d28e00826db75095"
# missing checkdepends
options = ["!check"]

if self.profile().arch == "riscv64":
    # ld: error: section size decrease is too large
    tool_flags = {"CFLAGS": ["-mno-relax"]}

def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

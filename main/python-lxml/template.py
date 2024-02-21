pkgname = "python-lxml"
pkgver = "5.1.0"
pkgrel = 0
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
pkgdesc = "Python bindings for the libxml2 and libxslt libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND custom:ElementTree"
url = "https://lxml.de"
source = f"https://github.com/lxml/lxml/archive/lxml-{pkgver}.tar.gz"
sha256 = "26c83dd0e6866a53d15606c3175d84cecb524e8bad6b8bfdd6112dc037c6be64"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSES.txt")
    self.install_license("doc/licenses/BSD.txt")
    self.install_license("doc/licenses/elementtree.txt")

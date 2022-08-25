pkgname = "python-charset-normalizer"
pkgver = "2.1.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Encoding and language detection"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://charset-normalizer.readthedocs.io"
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f4235706cfc5b3e8f3519abbefbca21442e46a073b8e3ab74ec949e181ac9e4c"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

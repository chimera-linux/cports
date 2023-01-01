pkgname = "python-charset-normalizer"
pkgver = "3.0.0"
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
sha256 = "7988228e24f8e3fdca28dde813ea3e8bbefb8ecea609a3c34230689fe50b054d"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

pkgname = "python-charset-normalizer"
pkgver = "2.0.7"
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
sha256 = "6473e80f73f5918254953073798a367f120cc5717e70c917359e155901c0e2d0"
# dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")

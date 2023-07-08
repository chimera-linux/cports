pkgname = "python-charset-normalizer"
pkgver = "3.2.0"
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
sha256 = "8f8c0a09ab745efc68ce4c1b85292ded2f06ea106f8086f614a0a9403c3dde0a"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

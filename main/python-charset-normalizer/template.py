pkgname = "python-charset-normalizer"
pkgver = "3.1.0"
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
sha256 = "0ca96d2ffef13e7062c53df8619e97b910343d1e14b4b92ee71bc61d2d18ced4"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

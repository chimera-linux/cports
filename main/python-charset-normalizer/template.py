pkgname = "python-charset-normalizer"
pkgver = "2.0.12"
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
sha256 = "8dd3a1a5444741208d627993344516cb62909c8c3f5c55deaa5bee6a305ead7a"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

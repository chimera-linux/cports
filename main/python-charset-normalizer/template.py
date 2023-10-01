pkgname = "python-charset-normalizer"
pkgver = "3.3.0"
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
sha256 = "bf2970e07cae5d97f71861e856e8d4114d995285ffa8ca536776c1c04fd46943"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

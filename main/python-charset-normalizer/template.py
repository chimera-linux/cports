pkgname = "python-charset-normalizer"
pkgver = "3.4.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Encoding and language detection"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://charset-normalizer.readthedocs.io"
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz>3.4.0-real.tar.gz"
sha256 = "e8dfa606a7c3f4d4540e7f648a602338323ee0f5e458043accf59b4a0493783f"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

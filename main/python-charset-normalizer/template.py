pkgname = "python-charset-normalizer"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Encoding and language detection"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://charset-normalizer.readthedocs.io"
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "941da22c392255f0ed212ce3ef2a78abd69f3c3a6fcbb2a42dfb7f678d4c09bd"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

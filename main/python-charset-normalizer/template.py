pkgname = "python-charset-normalizer"
pkgver = "3.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Encoding and language detection"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://charset-normalizer.readthedocs.io"
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz>3.4.0-real.tar.gz"
sha256 = "5b91677d4c790eead798f4ed3e5f546ed80d6fe8cf1d8120939960d593371855"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

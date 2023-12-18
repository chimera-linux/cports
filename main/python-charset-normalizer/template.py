pkgname = "python-charset-normalizer"
pkgver = "3.3.2"
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
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9948e5c17831916ef192cf3f26c744d539eb6f4e9e3b02eea649552c52b10d91"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

pkgname = "python-charset-normalizer"
pkgver = "3.4.2"
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
license = "MIT"
url = "https://charset-normalizer.readthedocs.io"
source = f"https://github.com/Ousret/charset_normalizer/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c0053743def688759bd8d4512dc93ae7b0514c217e8505a09bbbda84698ea3e9"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

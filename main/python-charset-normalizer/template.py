pkgname = "python-charset-normalizer"
pkgver = "3.3.1"
pkgrel = 0
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
sha256 = "82fba49093b118ecb75724413d5838c66b3269491aecda33199e17b5487a3444"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

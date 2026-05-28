pkgname = "python-charset-normalizer"
pkgver = "3.4.7"
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
sha256 = "7cf0421a9ac9f5b0894764a6756053e01f1f68641ed6377dfb21c776ca7031ca"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

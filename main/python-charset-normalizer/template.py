pkgname = "python-charset-normalizer"
pkgver = "3.4.3"
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
sha256 = "a8e48df4c97e52bc516e27edb301cd837684bb7266ce44a3532a9eed429c9e1c"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

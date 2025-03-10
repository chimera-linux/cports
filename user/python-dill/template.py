pkgname = "python-dill"
pkgver = "0.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python serialization library"
license = "BSD-3-Clause"
url = "https://github.com/uqfoundation/dill"
source = f"$(PYPI_SITE)/d/dill/dill-{pkgver}.tar.gz"
sha256 = "0633f1d2df477324f53a895b02c901fb961bdbf65a17122586ea7019292cbcf0"
# broken test module import
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

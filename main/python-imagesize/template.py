pkgname = "python-imagesize"
pkgver = "2.0.0"
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
pkgdesc = "Python3 library to get image size from png/jpeg/jpeg2000/gif file"
license = "MIT"
url = "https://github.com/shibukawa/imagesize_py"
source = f"$(PYPI_SITE)/i/imagesize/imagesize-{pkgver}.tar.gz"
sha256 = "8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

pkgname = "python-imagesize"
pkgver = "1.4.1"
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
pkgdesc = "Python3 library to get image size from png/jpeg/jpeg2000/gif file"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shibukawa/imagesize_py"
source = f"$(PYPI_SITE)/i/imagesize/imagesize-{pkgver}.tar.gz"
sha256 = "69150444affb9cb0d5cc5a92b3676f0b2fb7cd9ae39e947a5e11a36b4497cd4a"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")

pkgname = "python-imagesize"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python3 library to get image size from png/jpeg/jpeg2000/gif file"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shibukawa/imagesize_py"
source = f"$(PYPI_SITE)/i/imagesize/imagesize-{pkgver}.tar.gz"
sha256 = "cd1750d452385ca327479d45b64d9c7729ecf0b3969a58148298c77092261f9d"
# dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE.rst")

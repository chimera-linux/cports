pkgname = "python-evdev"
pkgver = "1.6.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
makedepends = ["python-devel", "linux-headers"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for evdev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/gvalkov/python-evdev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6b412da2d3b206feff86bb3b6456b8dde8e2b0b9ce23dfd4e556ced125c6ac4f"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

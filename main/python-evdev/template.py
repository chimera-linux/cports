pkgname = "python-evdev"
pkgver = "1.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel", "linux-headers"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for evdev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/gvalkov/python-evdev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9f09ccbb89880dd82c7f71482b662fb1ebb5824968cac0cd3d4e50b9f7715f6a"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

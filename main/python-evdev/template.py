pkgname = "python-evdev"
pkgver = "1.9.0"
pkgrel = 1
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
license = "BSD-3-Clause"
url = "https://github.com/gvalkov/python-evdev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9783a80dca381b9258f74a80a8f7be3fcd7e1c8206752bc428b1b88be22ab369"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

pkgname = "python-evdev"
pkgver = "1.9.1"
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
license = "BSD-3-Clause"
url = "https://github.com/gvalkov/python-evdev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "958e8aad958250428a57ff6c6fb8e2c254737affaca654165d9222f5a279698b"
# tests want /dev/uinput
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

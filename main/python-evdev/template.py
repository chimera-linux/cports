pkgname = "python-evdev"
pkgver = "1.9.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel", "linux-headers"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for evdev"
license = "BSD-3-Clause"
url = "https://github.com/gvalkov/python-evdev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1cfb65765b8c63e587110d9b42fa26806bd6dd76565c55c3618afd4c4c48c5a5"
# tests want /dev/uinput
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

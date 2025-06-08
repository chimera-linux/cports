pkgname = "python-libevdev"
pkgver = "0.12"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "libevdev"]
checkdepends = ["python-pytest", "libevdev"]
pkgdesc = "Python wrapper around libevdev"
license = "MIT"
url = "https://gitlab.freedesktop.org/libevdev/python-libevdev"
source = f"{url}/-/archive/{pkgver}/python-libevdev-{pkgver}.tar.gz"
sha256 = "9da0a5f686e0c68c0f2414f84313dc8ca7df0dea76abbd918b18c9abaf798316"


def post_install(self):
    self.install_license("COPYING")

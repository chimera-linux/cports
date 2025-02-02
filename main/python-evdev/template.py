pkgname = "python-evdev"
pkgver = "1.8.0"
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
sha256 = "886a7d55fd734ec9bda65e3620d401ad3147201ea9dbc086ca5dbb3e70c505b5"
# can't find itself
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

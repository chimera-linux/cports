pkgname = "scons"
pkgver = "4.8.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Build system nobody likes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://scons.org"
source = f"https://github.com/SCons/scons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9735ac24f345a11c76561991e3c3bdf943f97c772ded54156243e7f4ea5f4bc5"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

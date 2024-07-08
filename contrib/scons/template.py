pkgname = "scons"
pkgver = "4.8.0"
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
sha256 = "e9e0cc15f0a304f58cc9a860ab1520feb3e92b2dcc42131ecb94c30829dd1887"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

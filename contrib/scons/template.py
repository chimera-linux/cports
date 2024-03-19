pkgname = "scons"
pkgver = "4.7.0"
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
sha256 = "0182f95eecacb4a0effa89e5b2f1e0f7b5ea9f6e6b331e8486f0ce81b05bbb47"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

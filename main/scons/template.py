pkgname = "scons"
pkgver = "4.9.1"
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
license = "MIT"
url = "https://scons.org"
source = f"https://github.com/SCons/scons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "810c3f82c23758f8eaa23f7263363e1ac1822253dc8719ffa897ee77604bbe02"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

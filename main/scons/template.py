pkgname = "scons"
pkgver = "4.10.0"
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
sha256 = "d50b70e9a89e984cc0f4f4456fa4f8da6845c8dd284d8e833ab6baac9f84fbc6"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

pkgname = "scons"
pkgver = "4.6.0"
pkgrel = 1
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
sha256 = "085fc9df961224b91ed715c5c44a11796a3e614d146139989ab14e8a347425ff"
# uhhh, nah
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

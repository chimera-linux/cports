pkgname = "nyacme"
pkgver = "1.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-dnspython",
    "uacme",
]
pkgdesc = "Wrapper for uacme"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://git.ddd.rip/ptrcnull/nyacme"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "07e0e33c3d6fc166474c5120790140fac2ecddcf94394228e969e5c7cc05442c"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

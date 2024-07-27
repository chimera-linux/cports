pkgname = "nyacme"
pkgver = "0.1.14"
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
sha256 = "4a7125ec4d02ab64bea58e6d28d81a829ad50b4bd81c188e57d6735e8f5156d2"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

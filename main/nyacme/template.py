pkgname = "nyacme"
pkgver = "1.1.2"
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
license = "BSD-2-Clause"
url = "https://git.ddd.rip/ptrcnull/nyacme"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3939997278d696167b1ede81a45d8ff222fa0a268d4f49bf277e2006ada99ea2"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

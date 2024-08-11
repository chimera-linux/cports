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
sha256 = "647dc66e6b87b8dbdb4dc15979b90076cd2cdc40ba733e7d7cb5ed2edd07b4d6"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

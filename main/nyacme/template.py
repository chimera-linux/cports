pkgname = "nyacme"
pkgver = "1.1.0"
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
sha256 = "7c5675e72eb48f5b07ecb0acb620de8cd9822760294d8e60d2e3c131f993bc30"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

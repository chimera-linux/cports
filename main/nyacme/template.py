pkgname = "nyacme"
pkgver = "1.0.3"
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
sha256 = "0f31fcda2c8de31289d10fec2dde6c7652a354fae533ad3ab3647a375272afa4"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

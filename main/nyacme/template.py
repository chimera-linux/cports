pkgname = "nyacme"
pkgver = "1.0.2"
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
sha256 = "5552c43359b886cb6a532ecf55e62a4bf5f209e758497292bb1f6eca902196df"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

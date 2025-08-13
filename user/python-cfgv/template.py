pkgname = "python-cfgv"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-setuptools",
]
checkdepends = [
    "python-installer",
    "python-pytest",
]
depends = [
    "python",
]
pkgdesc = "Validate configuration and produce human readable error messages"
license = "MIT"
url = "https://github.com/asottile/cfgv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a8a4e4ad5618b6e65af563b14f46ccb1e45f5725c3b733d0ba15bb2a3b5bf9fd"


def post_install(self):
    self.install_license("LICENSE")

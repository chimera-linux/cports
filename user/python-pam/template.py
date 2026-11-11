pkgname = "python-pam"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["linux-pam", "python-pytest"]
depends = ["linux-pam"]
pkgdesc = "Python interface to PAM"
license = "MIT"
url = "https://github.com/FirefighterBlu3/python-pam"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8165f7cbbf2aa4c7f167de350d5218c4eb366b1756cd0538ab581c04377682c6"


def post_install(self):
    self.install_license("LICENSE")

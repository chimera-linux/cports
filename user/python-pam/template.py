pkgname = "python-pam"
pkgver = "2.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-six",
]
checkdepends = ["linux-pam", "python-pytest"]
depends = ["linux-pam", "python-six"]
pkgdesc = "Python PAM module"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "MIT"
url = "https://github.com/FirefighterBlu3/python-pam"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "23f5fd680b43d9dc8c96061c2c855f7c4758ee29c5d9f3cc469b558a0afd558b"


def post_install(self):
    self.install_license("LICENSE")

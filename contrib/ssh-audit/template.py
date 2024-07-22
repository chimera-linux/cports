pkgname = "ssh-audit"
pkgver = "3.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "SSH server & client configuration auditor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jtesta/ssh-audit"
source = f"{url}/releases/download/v{pkgver}/ssh-audit-{pkgver}.tar.gz"
sha256 = "db21007cb84ac95fa899bdb8f35bb4102a9fd28fc8225c5d16ced4ab8aa0413b"


def post_install(self):
    self.install_man("ssh-audit.1")
    self.install_license("LICENSE")

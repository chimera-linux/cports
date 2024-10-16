pkgname = "ssh-audit"
pkgver = "3.3.0"
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
sha256 = "e533c9ff2c1e655576b78a7732cdb01cf765e002716e5c086322ba4737c5e63b"


def post_install(self):
    self.install_man("ssh-audit.1")
    self.install_license("LICENSE")

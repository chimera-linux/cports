pkgname = "ssh-audit"
pkgver = "3.1.0"
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
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bea22074aa13f61cbe8e6876912a7eb5796569d980a7429deef112dc51ffd604"


def post_install(self):
    self.install_man("ssh-audit.1")
    self.install_license("LICENSE")

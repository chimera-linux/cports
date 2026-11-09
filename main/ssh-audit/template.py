pkgname = "ssh-audit"
pkgver = "3.9.0"
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
license = "MIT"
url = "https://github.com/jtesta/ssh-audit"
source = f"{url}/releases/download/v{pkgver}/v{pkgver}.tar.gz"
sha256 = "618ec29801c3abefcef8bb8177f918dcba6b3542f0803ce510cd13bfcd13815d"


def post_install(self):
    self.install_man("ssh-audit.1")
    self.install_license("LICENSE")

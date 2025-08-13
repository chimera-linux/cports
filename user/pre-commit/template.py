pkgname = "pre-commit"
pkgver = "4.3.0"
pkgrel = 0
hostmakedepends = [
    "python-setuptools",
]
depends = [
    "bash",
    "git",
    "python-cfgv",
    "python-identify",
    "python-nodeenv",
    "python-pyyaml",
    "python-virtualenv",
]
pkgdesc = "Git pre-commit hook framework"
license = "MIT"
url = "https://pre-commit.com"
source = f"https://github.com/pre-commit/pre-commit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fdcb25e1e93426362988efabecd55b1540fcd1f613ef42c5320eb299a35debec"


def build(self):
    self.do("python", "setup.py", "build")


def install(self):
    self.do(
        "python",
        "setup.py",
        "install",
        "--prefix=/usr",
        f"--root={self.chroot_destdir}",
    )
    self.install_license("LICENSE")

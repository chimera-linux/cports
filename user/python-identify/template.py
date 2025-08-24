pkgname = "python-identify"
pkgver = "2.6.13"
pkgrel = 0
hostmakedepends = [
    "python-setuptools",
]
depends = [
    "python",
]
pkgdesc = "File identification library for Python"
license = "MIT"
url = "https://github.com/pre-commit/identify"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "93a51afb4721ebbcc46045af64e26b063fd691cfb966b26c21999e028eeeb12e"


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

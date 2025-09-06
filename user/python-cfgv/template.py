pkgname = "python-cfgv"
pkgver = "3.4.0"
pkgrel = 0
hostmakedepends = [
    "python-setuptools",
]
depends = [
    "python",
]
pkgdesc = "Validate configuration and produce human readable error messages"
license = "MIT"
url = "https://github.com/asottile/cfgv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a8a4e4ad5618b6e65af563b14f46ccb1e45f5725c3b733d0ba15bb2a3b5bf9fd"


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

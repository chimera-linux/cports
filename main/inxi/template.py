pkgname = "inxi"
pkgver = "3.3.38.1"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{pkgver[: pkgver.rfind('.')]}-{pkgver[pkgver.rfind('.') + 1 :]}.tar.gz"
sha256 = "9601b5d6287a2508a2e3c2652ce44190636dfe48371dc658e48ffc74af500b1b"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

pkgname = "inxi"
pkgver = "3.3.39.1"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{pkgver[: pkgver.rfind('.')]}-{pkgver[pkgver.rfind('.') + 1 :]}.tar.gz"
sha256 = "c0441f21dc5ea365a6d63466070d00e6858aed3b3c42276a1bf18ab3c57c013c"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

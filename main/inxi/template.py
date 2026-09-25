pkgname = "inxi"
pkgver = "3.3.41.1"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{pkgver[: pkgver.rfind('.')]}-{pkgver[pkgver.rfind('.') + 1 :]}.tar.gz"
sha256 = "e08d92550a0f10890e722cc7db1e6d6cbde7e9fb47e61a8c6cec51f54a0b63d8"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

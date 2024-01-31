pkgname = "inxi"
_pver = "3.3.32-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "e7a7f7b4f16e023a54c79512e825b4a9d1819cf42d587c729b73d0332ab074bc"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

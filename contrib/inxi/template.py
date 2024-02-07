pkgname = "inxi"
_pver = "3.3.33-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "c2d7ae8914f2810d4377999c24d3839fa9a757a6ace59ff57ab366873161d38c"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

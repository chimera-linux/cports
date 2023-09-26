pkgname = "inxi"
_pver = "3.3.30-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "650712b94bc6b71b51f579ae293b920252f73086c242ddf86270c84bc8128d53"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

pkgname = "inxi"
_pver = "3.3.31-2"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "0f4dd81980b327aa71f3684a832ec4488721024d428c712f3c9bbdb35f6a2b42"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

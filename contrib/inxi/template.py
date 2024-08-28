pkgname = "inxi"
_pver = "3.3.35-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{_pver}.tar.gz"
sha256 = "08e43312bc60435d770607c3611f2fa35478ea0f48c60d5d5fd60ab2ee421f2e"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

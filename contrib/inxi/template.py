pkgname = "inxi"
_pver = "3.3.34-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "7cfc5c0abe10cb59f281733ce1d526583312344007756e7713fd5c51200b80fb"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

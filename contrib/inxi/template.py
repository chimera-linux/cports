pkgname = "inxi"
_pver = "3.3.31-3"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"https://codeberg.org/smxi/inxi/archive/{_pver}.tar.gz"
sha256 = "24f0a807ed4771590de851f98a64ed9b3f8b5a331f99a5edecbcc7ad59fbe7db"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

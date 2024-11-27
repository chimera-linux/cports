pkgname = "inxi"
_pver = "3.3.36-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{_pver}.tar.gz"
sha256 = "0f1e0ac7d5b702e66aec8fc3c07aaba036c0d47e729c35f26f19cddaa0b234d2"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

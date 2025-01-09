pkgname = "inxi"
_pver = "3.3.37-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{_pver}.tar.gz"
sha256 = "da730f84f4a2ca53bab471860a83995c9d498bb34c2518fbb7ff65ee705e048e"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")

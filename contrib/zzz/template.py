pkgname = "zzz"
pkgver = "20231124"
pkgrel = 0
pkgdesc = "Simple script to suspend or hibernate your computer"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "custom:none"
url = "https://github.com/void-linux/void-runit"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2bdb86a08ee0ee70d1a189ebbf9e60157f847e8c8f75caedc009536ca794a77c"


def do_install(self):
    self.install_bin("zzz")
    self.install_man("zzz.8")

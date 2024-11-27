pkgname = "game-devices-udev"
pkgver = "0.23"
pkgrel = 1
pkgdesc = "Miscellaneous udev rules for game devices"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://codeberg.org/fabiscafe/game-devices-udev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9eb09eea9b66692cbe076e74a649957a091ae4b8ae07ea51fe08693ecb48b521"


def install(self):
    self.install_license("LICENSE")
    self.install_file("*.rules", "usr/lib/udev/rules.d", glob=True)

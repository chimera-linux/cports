pkgname = "game-devices-udev"
pkgver = "0.22"
pkgrel = 0
pkgdesc = "Miscellaneous udev rules for game devices"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/fabiscafe/game-devices-udev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "bb490a48dcd6066ec0aedad618cf9e636586442597c2b8d2496be1be4263a9fc"


def do_install(self):
    self.install_license("LICENSE")
    self.install_file("*.rules", "usr/lib/udev/rules.d", glob=True)

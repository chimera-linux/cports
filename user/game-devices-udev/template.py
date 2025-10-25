pkgname = "game-devices-udev"
pkgver = "0.25"
pkgrel = 0
pkgdesc = "Miscellaneous udev rules for game devices"
license = "MIT"
url = "https://codeberg.org/fabiscafe/game-devices-udev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "5279e54d55fdaba63bf04bcef8ae0bd7f3232d8720739abdaf03bd83aa887c3a"


def install(self):
    self.install_license("LICENSE")
    self.install_file("*.rules", "usr/lib/udev/rules.d", glob=True)

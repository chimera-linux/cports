pkgname = "opsec"
pkgver = "0.0.2"
pkgrel = 0

pkgdesc = "Simple joke shell script with fake hacking tools"
license = "GPL-3.0-only"
url = "https://codeberg.org/vimsim/opsec"

source = f"https://codeberg.org/vimsim/opsec/releases/download/v{pkgver}/v{pkgver}.tar.gz"
sha256 = "85b2e9c9188b924f334d90fd92f9ff50ab691e043d13241188f52a7c07f2c5d6"


def install(self):
    self.install_bin("opsec.sh", name="opsec")
    self.install_license("LICENSE")

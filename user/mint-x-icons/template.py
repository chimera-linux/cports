pkgname = "mint-x-icons"
pkgver = "1.8.0"
pkgrel = 0
depends = ["hicolor-icon-theme"]
pkgdesc = "Mint-X icon theme"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxmint/mint-x-icons"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f208a47169934649d480f572c1d3ebcb879fd33877176ecbcf3ce8a49adca112"


def install(self):
    self.install_files("usr", "")

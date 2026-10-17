pkgname = "mint-y-icons"
pkgver = "1.9.7"
pkgrel = 0
depends = ["hicolor-icon-theme"]
pkgdesc = "Mint-Y icon theme"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxmint/mint-y-icons"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f561f324a60da03a8bbcd5d5191d56717539d70527c452d988b8563b390a4140"


def install(self):
    self.install_files("usr", "")

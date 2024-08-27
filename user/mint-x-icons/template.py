pkgname = "mint-x-icons"
pkgver = "1.7.1"
pkgrel = 0
pkgdesc = "Mint-X icon theme"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/mint"
source = f"https://github.com/linuxmint/mint-x-icons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "484555b81ba71a5dcee737c9defa5f45b53cd827eb9964d55cf48ef6a450a712"


def install(self):
    self.install_files("usr", "")

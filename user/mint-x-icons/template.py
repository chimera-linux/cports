pkgname = "mint-x-icons"
pkgver = "1.7.2"
pkgrel = 0
pkgdesc = "Mint-X icon theme"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/mint"
source = f"https://github.com/linuxmint/mint-x-icons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e459855e548fea2b0bd22d961742e91970286eeda46a8136d05e0d7b53b46373"


def install(self):
    self.install_files("usr", "")

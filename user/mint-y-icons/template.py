pkgname = "mint-y-icons"
pkgver = "1.7.9"
pkgrel = 0
pkgdesc = "Mint-Y icon theme"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "CC-BY-SA-4.0"
url = "https://projects.linuxmint.com/mint"
source = f"https://github.com/linuxmint/mint-y-icons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c2ed6f0b9d814c3c0bfbadcde30a9669e52e2563fbb2c4912ef268c97629b105"
broken_symlinks = [
    "usr/share/icons/Mint-Y/apps/*/*Uber*riter.png",
    "usr/share/icons/Mint-Y/apps/*/org.gnome.Tetravex.png",
]


def install(self):
    self.install_files("usr", "")

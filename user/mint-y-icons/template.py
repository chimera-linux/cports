pkgname = "mint-y-icons"
pkgver = "1.7.7"
pkgrel = 0
pkgdesc = "Mint-Y icon theme"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "CC-BY-SA-4.0"
url = "https://projects.linuxmint.com/mint"
source = f"https://github.com/linuxmint/mint-y-icons/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c026e8c7cb43b36ffc8ac803e20b3ea77fb988f6435d17019c85dcd50ea91bed"
broken_symlinks = [
    "usr/share/icons/Mint-Y/apps/*/*Uber*riter.png",
    "usr/share/icons/Mint-Y/apps/*/org.gnome.Tetravex.png",
]


def install(self):
    self.install_files("usr", "")

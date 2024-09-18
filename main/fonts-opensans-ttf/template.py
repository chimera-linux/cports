pkgname = "fonts-opensans-ttf"
pkgver = "3.003"
pkgrel = 1
_commit = "bd7e37632246368c60fdcbd374dbf9bad11969b6"
pkgdesc = "Open source sans-serif typeface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://fonts.google.com/specimen/Open+Sans"
source = f"https://github.com/googlefonts/opensans/archive/{_commit}.tar.gz"
sha256 = "a1b16d859522daa826fb093d791ee252a1627274ef1b90f2773d670eb73a2a92"


def install(self):
    self.install_file("fonts/ttf/*.ttf", "usr/share/fonts/opensans", glob=True)
    self.install_license("OFL.txt")

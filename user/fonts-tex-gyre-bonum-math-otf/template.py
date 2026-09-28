pkgname = "fonts-tex-gyre-bonum-math-otf"
pkgver = "1005"
pkgrel = 0
pkgdesc = "Math companion for TeX Gyre Bonum"
license = "custom:GFL"
url = "https://www.gust.org.pl/projects/e-foundry/tg-math"
source = f"{url}/download/texgyrebonum-math-{pkgver}.zip"
sha256 = "8f8dc6f52ff838201f581f20b4ab634508e6d4b1e2745fe5d6b7732e1df73290"
options = ["!distlicense"]


def install(self):
    self.install_file(
        "opentype/texgyrebonum-math.otf", "usr/share/fonts/tex-gyre"
    )

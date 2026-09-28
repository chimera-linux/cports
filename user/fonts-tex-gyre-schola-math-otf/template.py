pkgname = "fonts-tex-gyre-schola-math-otf"
pkgver = "1533"
pkgrel = 0
pkgdesc = "Math companion for TeX Gyre Schola"
license = "custom:GFL"
url = "https://www.gust.org.pl/projects/e-foundry/tg-math"
source = f"{url}/download/texgyreschola-math-{pkgver}.zip"
sha256 = "53560861144138e25f89f1f487126d21c81c5086364ffcf2c8e5e46e37ebbe00"
options = ["!distlicense"]


def install(self):
    self.install_file(
        "opentype/texgyreschola-math.otf", "usr/share/fonts/tex-gyre"
    )

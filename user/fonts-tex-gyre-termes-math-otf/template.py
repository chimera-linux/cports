pkgname = "fonts-tex-gyre-termes-math-otf"
pkgver = "1543"
pkgrel = 0
pkgdesc = "Math companion for TeX Gyre Termes"
license = "custom:GFL"
url = "https://www.gust.org.pl/projects/e-foundry/tg-math"
source = f"{url}/download/texgyretermes-math-{pkgver}.zip"
sha256 = "5875b39d3987cbe4258e5933a2292fbece870177053c5a8f495492769e2d4bb2"
options = ["!distlicense"]


def install(self):
    self.install_file(
        "opentype/texgyretermes-math.otf", "usr/share/fonts/tex-gyre"
    )

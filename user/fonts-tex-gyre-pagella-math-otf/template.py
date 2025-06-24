pkgname = "fonts-tex-gyre-pagella-math-otf"
pkgver = "1632"
pkgrel = 0
pkgdesc = "Math companion for TeX Gyre Pagella"
license = "custom:GFL"
url = "https://www.gust.org.pl/projects/e-foundry/tg-math"
source = f"{url}/download/texgyrepagella-math-{pkgver}.zip"
sha256 = "68a9c0ce195915334673960b13a281f24d31a8ae380454a0e35652dba506d474"
options = ["!distlicense"]


def install(self):
    self.install_file(
        "opentype/texgyrepagella-math.otf", "usr/share/fonts/tex-gyre"
    )

pkgname = "fonts-tex-gyre-otf"
pkgver = "2.501"
pkgrel = 0
pkgdesc = "TeX Gyre Collection of Fonts"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "OFL-1.1"
url = "https://www.gust.org.pl/projects/e-foundry/tex-gyre/index_html"
source = f"https://www.gust.org.pl/projects/e-foundry/tex-gyre/whole/tg{pkgver.replace('.', '_')}otf.zip"
sha256 = "d7f8be5317bec4e644cf16c5abf876abeeb83c43dbec0ccb4eee4516b73b1bbe"


def install(self):
    self.install_file("*.otf", "usr/share/fonts/tex-gyre", glob=True)

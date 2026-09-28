pkgname = "fonts-tex-gyre-otf"
pkgver = "2.609"
_pkgdate = "31_03_2026"
pkgrel = 0
pkgdesc = "TeX Gyre Collection of Fonts"
license = "OFL-1.1"
url = "https://www.gust.org.pl/projects/e-foundry/tex-gyre/index_html"
source = f"https://www.gust.org.pl/projects/e-foundry/tex-gyre/whole/tex_gyre-otf-{pkgver.replace('.', '_')}-{_pkgdate}.zip"
sha256 = "1731555aea263ad82e7f555fb6483ec98342593d63822f658f7a9f8023d85a33"
# No license in tarball
options = ["!distlicense"]


def install(self):
    self.install_file("*.otf", "usr/share/fonts/tex-gyre", glob=True)

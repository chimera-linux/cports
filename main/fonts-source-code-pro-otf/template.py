pkgname = "fonts-source-code-pro-otf"
pkgver = "2.038"
_itver = "1.058"
_vver = "1.018"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-code-pro"
source = f"https://github.com/adobe-fonts/source-code-pro/releases/download/{pkgver}R-ro/{_itver}R-it/{_vver}R-VAR/OTF-source-code-pro-{pkgver}R-ro-{_itver}R-it.zip"
sha256 = "478028ec70adc1ff73848a546c3ad266716a0096cd1f1a1ef18aeff0199d5996"

def do_install(self):
    for f in self.cwd.glob("*.otf"):
        self.install_file(f, "usr/share/fonts/source-code-pro")

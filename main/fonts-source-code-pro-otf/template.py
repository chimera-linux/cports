pkgname = "fonts-source-code-pro-otf"
pkgver = "2.040"
_itver = "1.060"
_vver = "1.024"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-code-pro"
source = f"https://github.com/adobe-fonts/source-code-pro/releases/download/{pkgver}R-u/{_itver}R-i/{_vver}R-vf/OTF-source-code-pro-{pkgver}R-u_{_itver}R-i_{_vver}Rvf.zip"
sha256 = "98e0edc528b80fd58c7847b5829f151559b10bbc8bc56c3845b4833a14e20721"

def do_install(self):
    for f in self.cwd.glob("*.otf"):
        self.install_file(f, "usr/share/fonts/source-code-pro")

pkgname = "fonts-source-code-pro-otf"
pkgver = "2.042"
_itver = "1.062"
_vver = "1.026"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-code-pro"
source = f"https://github.com/adobe-fonts/source-code-pro/releases/download/{pkgver}R-u/{_itver}R-i/{_vver}R-vf/OTF-source-code-pro-{pkgver}R-u_{_itver}R-i.zip"
sha256 = "754a2e3ebb945ae905d720ac5896b3b34acc9546dd6551ef9536869788629dae"
# No license in tarball
options = ["!distlicense"]


def install(self):
    self.install_file("*.otf", "usr/share/fonts/source-code-pro", glob=True)

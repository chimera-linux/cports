pkgname = "fonts-source-sans-otf"
pkgver = "3.046"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-sans"
source = f"https://github.com/adobe-fonts/source-sans/releases/download/{pkgver}R/OTF-source-sans-{pkgver}R.zip"
sha256 = "ed03cdb943892e60ebb7f63f1ec8d826722923f7f65dd9f01fe99ce7a04b8cb8"

def do_install(self):
    for f in self.cwd.glob("*.otf"):
        self.install_file(f, "usr/share/fonts/source-sans")

pkgname = "fonts-source-sans-otf"
pkgver = "3.052"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-sans"
source = f"https://github.com/adobe-fonts/source-sans/releases/download/{pkgver}R/OTF-source-sans-{pkgver}R.zip"
sha256 = "a4ebbdea20b08ccbd7bf3665a9462454eefdd01d9a6307129d3b3d4672981074"
# No license in tarball
options = ["!distlicense"]


def install(self):
    self.install_file("OTF/*.otf", "usr/share/fonts/source-sans", glob=True)

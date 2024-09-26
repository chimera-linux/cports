pkgname = "fonts-libertinus-otf"
pkgver = "7.051"
pkgrel = 0
pkgdesc = "Fonts based on Linux Libertine/Biolinum, with extended math support"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "OFL-1.1"
url = "https://github.com/alerque/libertinus"
source = f"{url}/releases/download/v{pkgver}/Libertinus-{pkgver}.tar.zst"
sha256 = "250677c929d3775a30913643594379af264ac2ef2801035aa1dcbe30b9be23a6"


def install(self):
    self.install_file(
        "static/OTF/*.otf", "usr/share/fonts/libertinus", glob=True
    )
    self.install_license("OFL.txt")

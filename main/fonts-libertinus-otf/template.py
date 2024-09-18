pkgname = "fonts-libertinus-otf"
pkgver = "7.040"
pkgrel = 1
pkgdesc = "Fonts based on Linux Libertine/Biolinum, with extended math support"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "OFL-1.1"
url = "https://github.com/alerque/libertinus"
source = f"{url}/releases/download/v{pkgver}/Libertinus-{pkgver}.tar.xz"
sha256 = "7fe9f022722d1c1cc67dc2c28a110b3bb55bae3575196160d2422c89333b3850"


def install(self):
    self.install_file(
        "static/OTF/*.otf", "usr/share/fonts/libertinus", glob=True
    )
    self.install_license("OFL.txt")

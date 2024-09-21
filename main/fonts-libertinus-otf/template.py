pkgname = "fonts-libertinus-otf"
pkgver = "7.050"
pkgrel = 0
pkgdesc = "Fonts based on Linux Libertine/Biolinum, with extended math support"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "OFL-1.1"
url = "https://github.com/alerque/libertinus"
source = f"{url}/releases/download/v{pkgver}/Libertinus-{pkgver}.tar.zst"
sha256 = "cbb54c4c482376eb17bb6397494489baacff0755d3864f9b5c772e2f3d43d429"


def install(self):
    self.install_file(
        "static/OTF/*.otf", "usr/share/fonts/libertinus", glob=True
    )
    self.install_license("OFL.txt")

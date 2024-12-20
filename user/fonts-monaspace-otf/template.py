pkgname = "fonts-monaspace-otf"
pkgver = "1.101"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
maintainer = "BarryLhm <Lhm13144572810@outlook.com>"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "89006779394fb251a046ccaa23b875b1edced3687f1628b37c6418d8f5da63c5"


def install(self):
    self.install_file("fonts/otf/*.otf", "usr/share/fonts/monaspace", glob=True)
    self.install_license("LICENSE")

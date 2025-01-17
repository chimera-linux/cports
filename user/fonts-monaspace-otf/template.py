pkgname = "fonts-monaspace-otf"
pkgver = "1.200"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
maintainer = "BarryLhm <Lhm13144572810@outlook.com>"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "e72ae4dacfa7268ef75abca32fba01cc92ec187897d4deb99ecb843c088d3307"


def install(self):
    self.install_file("fonts/otf/*.otf", "usr/share/fonts/monaspace", glob=True)
    self.install_license("LICENSE")

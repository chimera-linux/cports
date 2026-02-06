pkgname = "fonts-monaspace-otf"
pkgver = "1.301"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "de66c90030b20e78a9421fe2645824f47b9dec9cf1f3e600b9713fdccaa1ac0d"


def install(self):
    self.install_file(
        "fonts/Static Fonts/*/*.otf", "usr/share/fonts/monaspace", glob=True
    )
    self.install_license("LICENSE")

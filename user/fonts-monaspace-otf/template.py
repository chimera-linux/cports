pkgname = "fonts-monaspace-otf"
pkgver = "1.400"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "1ac6b955ea8d3d34627ce165df85b5a6c323a54de4a50dda024589ace31fbe8d"


def install(self):
    self.install_file(
        "fonts/Static Fonts/*/*.otf", "usr/share/fonts/monaspace", glob=True
    )
    self.install_license("LICENSE")

pkgname = "scc"
pkgver = "3.2.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "69cce0b57e66c736169bd07943cdbe70891bc2ff3ada1f4482acbd1335adbfad"
# objcopy fails on ppc
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

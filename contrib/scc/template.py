pkgname = "scc"
pkgver = "3.1.0"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "bffea99c7f178bc48bfba3c64397d53a20a751dfc78221d347aabdce3422fd20"
# objcopy fails on ppc
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

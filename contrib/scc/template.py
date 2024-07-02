pkgname = "scc"
pkgver = "3.3.4"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3097e23532d9a254fe217c81557136c7ac5aa4d48a200b61b366330e5eaf7ce4"
# objcopy fails on ppc
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

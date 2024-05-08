pkgname = "scc"
pkgver = "3.3.2"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2bbfed4cf34bbe50760217b479331cf256285335556a0597645b7250fb603388"
# objcopy fails on ppc
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

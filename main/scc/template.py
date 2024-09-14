pkgname = "scc"
pkgver = "3.3.5"
pkgrel = 4
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "028869a7d053879a8e3f2872fdd792f165db13696918d08863475c638f08ef06"


def post_install(self):
    self.install_license("LICENSE")

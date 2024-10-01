pkgname = "scc"
pkgver = "3.4.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "bdedb6f32d1c3d73ac7e55780021c742bc8ed32f6fb878ee3e419f9acc76bdaa"


def post_install(self):
    self.install_license("LICENSE")

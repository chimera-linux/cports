pkgname = "scc"
pkgver = "3.7.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "447233f70ebcc24f1dafb27b093afdd17d3a1d662de96e8226130c5308b02d01"


def post_install(self):
    self.install_license("LICENSE")

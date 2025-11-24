pkgname = "scc"
pkgver = "3.5.0"
pkgrel = 7
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "161f5d9bb359c6440114b7d2e0f98d588c02aa66fbe474d7660b244687fefb70"


def post_install(self):
    self.install_license("LICENSE")

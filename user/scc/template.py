pkgname = "scc"
pkgver = "4.1.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4f3cf36010c542b10d5582afb91c668b26889160b184deee21b4319347030a7c"


def post_install(self):
    self.install_license("LICENSE")

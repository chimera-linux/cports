pkgname = "bore"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cargo"
makedepends = ["cargo"]
pkgdesc = "CLI tool for making tunnels to localhost"
maintainer = "LeFantome <fantome137@proton.me>"
license = "MIT"
url = "https://github.com/ekzhang/bore"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cf821106ed428314d825ebe2d09f1842f979eac7acbf0976ac9cd01853d65163"


def post_install(self):
    self.install_license("LICENSE")

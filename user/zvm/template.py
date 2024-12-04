pkgname = "zvm"
pkgver = "0.8.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cf681dc7cf67994094c7ac4c0c7075d972d5382d94fe4873e4722e195380cb61"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "zvm"
pkgver = "0.7.7"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3f8298bc0226a1ae0fd608b0d505133b23a30cc1c97a503af68be53115ef5539"


def post_install(self):
    self.install_license("LICENSE")

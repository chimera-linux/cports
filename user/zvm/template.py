pkgname = "zvm"
pkgver = "0.7.4"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff72b3beda8dac5bd8d7d9fddb3252460ed454285ad9acb20f24ac00b45db102"


def post_install(self):
    self.install_license("LICENSE")

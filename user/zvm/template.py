pkgname = "zvm"
pkgver = "0.7.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5817f33f5e879f6a30868816b78ddc99f9bd180c34ed1bb1860ec3a01c6e954c"


def post_install(self):
    self.install_license("LICENSE")

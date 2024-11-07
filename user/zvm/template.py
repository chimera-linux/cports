pkgname = "zvm"
pkgver = "0.7.9"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f81b04d52fb9f89d1bf65717e22fe7158c66e269fa7201340a7e3910ad7ab221"


def post_install(self):
    self.install_license("LICENSE")

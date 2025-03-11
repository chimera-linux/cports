pkgname = "zvm"
pkgver = "0.8.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6a950174567b099e6602142f5b8105c65a244de69c45337b5211e0eccb43d7cf"


def post_install(self):
    self.install_license("LICENSE")

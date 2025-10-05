pkgname = "zvm"
pkgver = "0.8.8"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aafeb40122acd549817f106d072a96910a5440feec41d0af9f99474d3e498a09"


def post_install(self):
    self.install_license("LICENSE")

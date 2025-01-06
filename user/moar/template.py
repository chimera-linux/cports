pkgname = "moar"
pkgver = "1.31.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
maintainer = "Biswapriyo Nath <nathbappai@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "741505c48342778a4312b35f75b2c87e6d6149e4909f2e6a29d80e9e86c4e91c"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

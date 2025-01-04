pkgname = "moar"
pkgver = "1.30.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
maintainer = "Biswapriyo Nath <nathbappai@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e20f8a8eefb2594b57f6253e6e44b00555b3aece63a3dcf0f8e9e9ba7700d58"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

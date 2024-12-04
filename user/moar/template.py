pkgname = "moar"
pkgver = "1.30.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
maintainer = "Biswapriyo Nath <nathbappai@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a26954fca06c95604a94b6f208f62eff247e50c8d239262322a13d0959074de1"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

pkgname = "moar"
pkgver = "1.31.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
maintainer = "Biswapriyo Nath <nathbappai@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2d699c8322788943b77165e3a246ac493dad6233d9855ac84194923dfdbb40f1"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

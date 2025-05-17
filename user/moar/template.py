pkgname = "moar"
pkgver = "1.31.6"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f25f48a7e98aae566bca81c191e21307a46e61478696da6c74b50b84d162e967"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

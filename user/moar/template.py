pkgname = "moar"
pkgver = "1.31.5"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2c03100e24f88163d808d52b7a5763c0fe731b29c46fd44a103a089c5429eb72"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")

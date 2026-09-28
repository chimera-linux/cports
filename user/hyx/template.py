pkgname = "hyx"
pkgver = "2026.01.11"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Terminal hex editor inspired by vim"
license = "MIT"
url = "https://yx7.cc/code"
source = f"{url}/hyx/hyx-{pkgver}.tar.xz"
sha256 = "550863c9e6a2c0e2618c16a562c8ee995e88c1d30e62abfdf4ecb819b3c4df54"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("hyx")
    self.install_license("license.txt")

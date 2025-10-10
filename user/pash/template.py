pkgname = "pash"
pkgver = "2.3.0"
pkgrel = 0
pkgdesc = "Simple password manager using GPG written in POSIX sh"
license = "MIT"
url = "https://github.com/dylanaraps/pash"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7ee6a649d80350b8b52b1b7ad78d687775a3cc145fecbd3a75d34865c31dd7ef"


def install(self):
    self.install_license("LICENSE.md")
    self.install_bin("pash")

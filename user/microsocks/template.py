pkgname = "microsocks"
pkgver = "1.0.5"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Multithreaded, small, efficient SOCKS5 server"
license = "MIT"
url = "https://github.com/rofl0r/microsocks"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "939d1851a18a4c03f3cc5c92ff7a50eaf045da7814764b4cb9e26921db15abc8"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("microsocks")


def post_install(self):
    self.install_license("COPYING")

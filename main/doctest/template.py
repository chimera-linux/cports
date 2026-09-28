pkgname = "doctest"
pkgver = "2.4.12"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDOCTEST_USE_STD_HEADERS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Single-header testing framework"
license = "MIT"
url = "https://github.com/doctest/doctest"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "73381c7aa4dee704bd935609668cf41880ea7f19fa0504a200e13b74999c2d70"


def post_install(self):
    self.install_license("LICENSE.txt")

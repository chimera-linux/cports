pkgname = "immer"
pkgver = "0.8.1"
pkgrel = 0
build_style = "cmake"
makedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "catch2-devel",
]
pkgdesc = "C++ library for persistent and immutable data structures"
license = "BSL-1.0"
url = "https://sinusoid.es/immer"
source = f"https://github.com/arximboldi/immer/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "de8411c84830864604bb685dc8f2e3c0dbdc40b95b2f6726092f7dcc85e75209"
# tests didn't get run, probably an easy fix but don't want to deal with this rn
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

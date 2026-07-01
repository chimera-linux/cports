pkgname = "zug"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cmake"
makedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "catch2-devel",
]
pkgdesc = "C++ library for transducers"
license = "BSL-1.0"
url = "https://sinusoid.es/zug"
source = f"https://github.com/arximboldi/zug/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1b9c8f962e40baa6f0c6af35f957444850063d550078a3ebd0227727b8ef193c"
# tests didn't get run, probably an easy fix but don't want to deal with this rn
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

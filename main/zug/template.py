pkgname = "zug"
pkgver = "0.1.2"
pkgrel = 0
build_style = "cmake"
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
depends = [
    "boost-devel",
]
checkdepends = [
    "catch2-devel",
    *depends,
]
pkgdesc = "C++ library for transducers"
license = "BSL-1.0"
url = "https://sinusoid.es/zug"
source = f"https://github.com/arximboldi/zug/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75ff666a4ce1615b3ca26abbb17b10f5cb5cf5f86c9c293ec430c34750d3ea27"


def post_install(self):
    self.install_license("LICENSE")

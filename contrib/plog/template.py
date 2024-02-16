pkgname = "plog"
pkgver = "1.1.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPLOG_BUILD_SAMPLES=OFF",
    "-DPLOG_BUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Portable, simple, and extensible C++ logging library"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/SergiusTheBest/plog"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "55a090fc2b46ab44d0dde562a91fe5fc15445a3caedfaedda89fe3925da4705a"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "mold"
pkgver = "2.38.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMOLD_USE_MIMALLOC=OFF",
    "-DMOLD_USE_SYSTEM_TBB=ON",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "blake3-devel",
    "linux-headers",
    "onetbb-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["binutils-common"]
pkgdesc = "High-performance linker"
license = "MIT"
url = "https://github.com/rui314/mold"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "14bfb259fd7d0a1fdce9b66f8ed2dd0b134d15019cb359699646afeee1f18118"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/share/doc/mold/LICENSE")

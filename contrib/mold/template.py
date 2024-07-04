pkgname = "mold"
pkgver = "2.32.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/rui314/mold"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f3c9a527d884c635834fe7d79b3de959b00783bf9446280ea274d996f0335825"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.third-party")
    self.uninstall("usr/share/doc/mold/LICENSE")

pkgname = "mold"
pkgver = "2.31.0"
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
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "High-performance linker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/rui314/mold"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3dc3af83a5d22a4b29971bfad17261851d426961c665480e2ca294e5c74aa1e5"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.third-party")
    self.rm(self.destdir / "usr/share/doc/mold/LICENSE")

pkgname = "mold"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMOLD_USE_MIMALLOC=OFF",
    "-DMOLD_USE_SYSTEM_TBB=ON",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "zstd-devel",
    "linux-headers",
    "onetbb-devel",
    "openssl-devel",
    "zlib-devel",
]
pkgdesc = "High-performance linker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/rui314/mold"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a32bec1282671b18ea4691855aed925ea2f348dfef89cb7689cd81273ea0c5df"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.third-party")
    self.rm(self.destdir / "usr/share/doc/mold/LICENSE")

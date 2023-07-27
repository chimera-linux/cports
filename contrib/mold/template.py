pkgname = "mold"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMOLD_USE_MIMALLOC=OFF",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["openssl-devel", "zlib-devel", "libzstd-devel", "linux-headers"]
pkgdesc = "High-performance linker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/rui314/mold"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2ae8a22db09cbff626df74c945079fa29c1e5f60bbe02502dcf69191cf43527b"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.third-party")
    self.rm(self.destdir / "usr/share/doc/mold/LICENSE")

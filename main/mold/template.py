pkgname = "mold"
pkgver = "2.40.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib",  # XXX drop libexec
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
sha256 = "d1ce09a69941f8158604c3edcc96c7178231e7dba2da66b20f5ef6e112c443b7"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/share/doc/mold/LICENSE")

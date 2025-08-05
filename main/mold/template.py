pkgname = "mold"
pkgver = "2.40.3"
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
sha256 = "308c10f480d355b9f9ef8bb414dfb5f4842bee87eb96b6a7666942f4036a0223"
# TODO: a portion of the tests fail, for various reasons, such as assuming
# presence of gcc, gnu grep, and various toolchain specifics; around 70%
# of the tests pass right now, fix the rest later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/share/doc/mold/LICENSE")

pkgname = "c-blosc"
pkgver = "1.21.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_BENCHMARKS=OFF",
    "-DBUILD_FUZZERS=OFF",
    "-DPREFER_EXTERNAL_LZ4=ON",
    "-DPREFER_EXTERNAL_ZLIB=ON",
    "-DPREFER_EXTERNAL_ZSTD=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "lz4-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Library optimised for binary data compression"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.blosc.org"
source = f"https://github.com/Blosc/c-blosc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9fcd60301aae28f97f1301b735f966cc19e7c49b6b4321b839b4579a0c156f38"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("c-blosc-devel")
def _(self):
    return self.default_devel()

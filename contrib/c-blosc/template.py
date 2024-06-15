pkgname = "c-blosc"
pkgver = "1.21.5"
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
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Library optimised for binary data compression"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.blosc.org"
source = f"https://github.com/Blosc/c-blosc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "32e61961bbf81ffea6ff30e9d70fca36c86178afd3e3cfa13376adec8c687509"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("c-blosc-devel")
def _devel(self):
    return self.default_devel()

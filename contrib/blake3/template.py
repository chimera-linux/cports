pkgname = "blake3"
pkgver = "1.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
cmake_dir = "c"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "BLAKE3 cryptographic hash implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "CC0-1.0 OR Apache-2.0"
url = "https://github.com/BLAKE3-team/BLAKE3"
source = (
    f"https://github.com/BLAKE3-team/BLAKE3/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "822cd37f70152e5985433d2c50c8f6b2ec83aaf11aa31be9fe71486a91744f37"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _devel(self):
    return self.default_devel()

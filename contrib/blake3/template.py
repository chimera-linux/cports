pkgname = "blake3"
pkgver = "1.5.0"
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
sha256 = "f506140bc3af41d3432a4ce18b3b83b08eaa240e94ef161eb72b2e57cdc94c69"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _devel(self):
    return self.default_devel()

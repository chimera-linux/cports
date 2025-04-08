pkgname = "blake3"
pkgver = "1.8.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DBLAKE3_USE_TBB=ON"]
cmake_dir = "c"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["onetbb-devel"]
pkgdesc = "BLAKE3 cryptographic hash implementation"
license = "CC0-1.0 OR Apache-2.0"
url = "https://github.com/BLAKE3-team/BLAKE3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fc2aac36643db7e45c3653fd98a2a745e6d4d16ff3711e4b7abd3b88639463dd"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _(self):
    return self.default_devel()

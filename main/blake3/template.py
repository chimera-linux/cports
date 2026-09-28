pkgname = "blake3"
pkgver = "1.8.7"
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
sha256 = "c6782a28842b1c0478524ac06a4f2ede784038ee298d6e2162c0b089c4306a3c"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _(self):
    return self.default_devel()

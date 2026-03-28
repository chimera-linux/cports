pkgname = "blake3"
pkgver = "1.8.4"
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
sha256 = "b5ee5f5c5e025eb2733ae3af8d4c0e53bb66dff35095decfd377f1083e8ac9be"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _(self):
    return self.default_devel()

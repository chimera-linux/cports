pkgname = "blake3"
pkgver = "1.5.4"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
cmake_dir = "c"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "BLAKE3 cryptographic hash implementation"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "CC0-1.0 OR Apache-2.0"
url = "https://github.com/BLAKE3-team/BLAKE3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ddd24f26a31d23373e63d9be2e723263ac46c8b6d49902ab08024b573fd2a416"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _(self):
    return self.default_devel()

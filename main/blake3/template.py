pkgname = "blake3"
pkgver = "1.5.5"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "CC0-1.0 OR Apache-2.0"
url = "https://github.com/BLAKE3-team/BLAKE3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6feba0750efc1a99a79fb9a495e2628b5cd1603e15f56a06b1d6cb13ac55c618"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _(self):
    return self.default_devel()

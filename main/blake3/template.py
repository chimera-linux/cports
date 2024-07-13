pkgname = "blake3"
pkgver = "1.5.2"
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
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1bc38cd3cc501458054c3bb473e5e00338d6175121424040079025ea305ddef3"
hardening = ["vis", "cfi"]


@subpackage("blake3-devel")
def _devel(self):
    return self.default_devel()

pkgname = "simdutf"
pkgver = "8.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library of SIMD-accelerated Unicode routines"
license = "MIT"
url = "https://github.com/simdutf/simdutf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "033a91b1d7d1cb818c1eff49e61faaa1b64a3a530d59ef9efef0195e56bda8b1"


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("simdutf-devel")
def _(self):
    return self.default_devel()

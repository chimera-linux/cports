pkgname = "varlink"
pkgver = "24.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
checkdepends = ["bash"]
pkgdesc = "C implementation of the varlink protocol"
license = "Apache-2.0"
url = "https://github.com/varlink/libvarlink"
source = (
    f"https://github.com/varlink/libvarlink/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ca3ecd13005309e0322bc64a26f2960e613f2a9a9cedee845865c2d042f73b3c"
# CFI: fails in tests
hardening = ["vis", "!cfi"]


@subpackage("varlink-devel")
def _(self):
    return self.default_devel()

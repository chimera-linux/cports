pkgname = "varlink"
pkgver = "24"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
checkdepends = ["bash"]
pkgdesc = "C implementation of the varlink protocol"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/varlink/libvarlink"
source = (
    f"https://github.com/varlink/libvarlink/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "0586263ab8f4e8e26a2f2f54830f8f92e403326663b10e14fcf1a6c95e9eab95"
# CFI: fails in tests
hardening = ["vis", "!cfi"]


@subpackage("varlink-devel")
def _(self):
    return self.default_devel()

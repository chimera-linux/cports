pkgname = "varlink"
pkgver = "23"
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
sha256 = "a5575e070e446e7c4486d424393950e6cb7a3b376ee20d517b0c13a876659a8d"
# CFI: fails in tests
hardening = ["vis", "!cfi"]


@subpackage("varlink-devel")
def _(self):
    return self.default_devel()

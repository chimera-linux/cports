pkgname = "inih"
pkgver = "53"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddistro_install=true",
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Simple ini parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/benhoyt/inih"
source = f"{url}/archive/r{pkgver}.tar.gz"
sha256 = "01b0366fdfdf6363efc070c2f856f1afa33e7a6546548bada5456ad94a516241"
options = ["lto"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("inih-static")
def _static(self):
    return self.default_static()

@subpackage("inih-devel")
def _devel(self):
    return self.default_devel()

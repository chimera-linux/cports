pkgname = "inih"
pkgver = "55"
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
sha256 = "ba55f8ae2a8caf0653f30f48567241e14ea916acfc13481f502d8a9c8f507f68"

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("inih-devel")
def _devel(self):
    return self.default_devel()

pkgname = "unshield"
pkgver = "1.5.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Utility for InstallShield CAB archive extraction"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/twogood/unshield"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "34cd97ff1e6f764436d71676e3d6842dc7bd8e2dd5014068da5c560fe4661f60"
# runner not integrated
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("unshield-libs")
def _(self):
    return self.default_libs()


@subpackage("unshield-devel")
def _(self):
    return self.default_devel()

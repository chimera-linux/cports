pkgname = "cgif"
pkgver = "0.5.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "Fast and lightweight GIF encoder"
license = "MIT"
url = "https://github.com/dloebl/cgif"
source = f"https://github.com/dloebl/cgif/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dcc7731e974ee77db75df26c99aca4d95f11ca2d267d870d42bce1e0d1e1e75f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cgif-devel")
def _(self):
    return self.default_devel()

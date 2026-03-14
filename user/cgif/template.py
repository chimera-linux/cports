pkgname = "cgif"
pkgver = "0.5.2"
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
sha256 = "d5e603309176334406d7e4f0063ed96924fe9b0368e8037df2614c0df67bb41b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cgif-devel")
def _(self):
    return self.default_devel()

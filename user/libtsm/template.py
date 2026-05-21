pkgname = "libtsm"
pkgver = "4.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel", "libxkbcommon-devel"]
pkgdesc = "Terminal emulator state machine"
license = "MIT"
url = "https://github.com/kmscon/libtsm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b06d1434a750b5e4981be9696a9f65bfd7b38fe2d8d24199d92f11394bb8459"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtsm-devel")
def _(self):
    return self.default_devel()

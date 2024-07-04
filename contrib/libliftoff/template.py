pkgname = "libliftoff"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libdrm-devel",
]
pkgdesc = "KMS plane library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libliftoff"
source = f"{url}/-/archive/v{pkgver}/libliftoff-{pkgver}.tar.gz"
sha256 = "53b059fa785f629420e7d37bd68f4b2a3e4f463dca5f691d8d805901d80c492d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libliftoff-devel")
def _devel(self):
    return self.default_devel()

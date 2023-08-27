pkgname = "libliftoff"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Db_ndebug=false"]
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
sha256 = "165cbfee6b8a56847cba5740b89651718b95547b8659899d555357de6b6c05ad"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libliftoff-devel")
def _dev(self):
    return self.default_devel()

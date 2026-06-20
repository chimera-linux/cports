pkgname = "neatvnc"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "aml-devel",
    "ffmpeg-devel",
    "gnutls-devel",
    "libdrm-devel",
    "libjpeg-turbo-devel",
    "mesa-gbm-devel",
    "pixman-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC server library"
license = "ISC"
url = "https://github.com/any1/neatvnc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "993dedc30e72981650770c04438e9759537e4677010e2dab5e792c39afe74601"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neatvnc-devel")
def _(self):
    return self.default_devel()

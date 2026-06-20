pkgname = "neatvnc"
pkgver = "1.0.1"
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
sha256 = "c37678fb1f9bbb8bd0932eb6dbd68bf10e937777c376c6c278ed37510b2cbd4b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neatvnc-devel")
def _(self):
    return self.default_devel()

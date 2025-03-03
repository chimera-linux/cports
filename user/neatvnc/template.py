pkgname = "neatvnc"
pkgver = "0.9.4"
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
sha256 = "806e8420a1b9479c7f289ab01146affb320fce724cec3fda66242fd7e5eced0b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neatvnc-devel")
def _(self):
    return self.default_devel()

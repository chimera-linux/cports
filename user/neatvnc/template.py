pkgname = "neatvnc"
pkgver = "0.9.3"
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
sha256 = "110b440d63b87c0adab1e92a3c3126a05a06191a15b1454706e4b1d62344418b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neatvnc-devel")
def _(self):
    return self.default_devel()

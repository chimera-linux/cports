pkgname = "neatvnc"
pkgver = "0.9.2"
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
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://github.com/any1/neatvnc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1efa6080b47371d6bc44f627d6692fae4f2ea2faf30faad3462bbbb3c503e17c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neatvnc-devel")
def _(self):
    return self.default_devel()

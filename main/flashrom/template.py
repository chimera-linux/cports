pkgname = "flashrom"
pkgver = "1.4.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Duse_internal_dmi=false"]
hostmakedepends = ["meson", "pkgconf", "python-sphinx"]
makedepends = [
    "libftdi1-devel",
    "libusb-devel",
    "linux-headers",
    "pciutils-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["cmocka-devel"]
pkgdesc = "Utility for flashing ROM chips"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.flashrom.org"
source = f"https://download.flashrom.org/releases/flashrom-{pkgver}.tar.xz"
sha256 = "ad7ee1b49239c6fb4f8f55e36706fcd731435db1a4bd2fab3d80f1f72508ccee"
# needs special configuration?
options = ["!check", "linkundefver"]


@subpackage("flashrom-devel")
def _(self):
    return self.default_devel()


@subpackage("flashrom-libs")
def _(self):
    return self.default_libs()

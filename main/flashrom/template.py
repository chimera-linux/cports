pkgname = "flashrom"
pkgver = "1.3.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Duse_internal_dmi=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libftdi1-devel",
    "libusb-devel",
    "linux-headers",
    "pciutils-devel",
    "zlib-devel",
]
checkdepends = ["cmocka-devel"]
pkgdesc = "Utility for flashing ROM chips"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.flashrom.org"
source = f"https://download.flashrom.org/releases/flashrom-v{pkgver}.tar.bz2"
sha256 = "a053234453ccd012e79f3443bdcc61625cf97b7fd7cb4cdd8bfbffbe8b149623"
# needs special configuration?
options = ["!check", "linkundefver"]


@subpackage("flashrom-devel")
def _devel(self):
    return self.default_devel()


@subpackage("flashrom-libs")
def _libs(self):
    return self.default_libs()

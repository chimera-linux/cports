pkgname = "libftdi1"
pkgver = "1.5"
pkgrel = 6
build_style = "cmake"
configure_args = ["-DLIB_SUFFIX="]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libconfuse-devel", "libusb-devel"]
checkdepends = ["boost-devel"]
pkgdesc = "Library for communicating with FTDI USB devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later AND GPL-2.0-only"
url = "https://www.intra2net.com/en/developer/libftdi/download.php"
source = f"https://www.intra2net.com/en/developer/libftdi/download/libftdi1-{pkgver}.tar.bz2"
sha256 = "7c7091e9c86196148bd41177b4590dccb1510bfe6cea5bf7407ff194482eb049"
# testing setup is weirdly broken
options = ["!check"]


@subpackage("libftdi1-devel")
def _(self):
    return self.default_devel()

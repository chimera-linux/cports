pkgname = "pcsc-lite"
pkgver = "2.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibsystemd=false",
    "-Dlibudev=true",
    "-Dpolkit=true",
    "-Dusb=true",
]
hostmakedepends = ["flex", "meson", "perl", "pkgconf"]
makedepends = ["libusb-devel", "udev-devel", "polkit-devel"]
pkgdesc = "Middleware to access PC/SC smart cards using SCard API"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://pcsclite.apdu.fr"
source = f"https://pcsclite.apdu.fr/files/pcsc-lite-{pkgver}.tar.xz"
sha256 = "1acca22d2891d43ffe6d782740d32e78150d4fcc99e8a3cc763abaf546060d3d"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _(self):
    return self.default_devel()

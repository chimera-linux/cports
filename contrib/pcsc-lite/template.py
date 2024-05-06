pkgname = "pcsc-lite"
pkgver = "2.2.0"
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
pkgdesc = "Middleware to access a smart card using SCard API (PC/SC)"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://pcsclite.apdu.fr"
source = f"https://pcsclite.apdu.fr/files/pcsc-lite-{pkgver}.tar.xz"
sha256 = "76e06bb9f47f0c10c4eaec3ee9cea634bda28a1fc46f1286c097d220386c22d4"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()

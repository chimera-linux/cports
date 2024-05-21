pkgname = "pcsc-lite"
pkgver = "2.2.2"
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
sha256 = "04edaed13565aab0fa7c711382be2b02e38faffbccd024ab68085ffb7091be22"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()

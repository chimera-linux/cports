pkgname = "pcsc-lite"
pkgver = "2.3.1"
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
sha256 = "a641d44d57affe1edd8365dd75307afc307e7eefb4e7ad839f6f146baa41ed56"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _(self):
    return self.default_devel()

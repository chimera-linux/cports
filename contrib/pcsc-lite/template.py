pkgname = "pcsc-lite"
pkgver = "2.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-libsystemd"]
configure_gen = []
hostmakedepends = ["pkgconf", "flex", "perl"]
makedepends = ["libusb-devel", "udev-devel", "polkit-devel"]
pkgdesc = "Middleware to access a smart card using SCard API (PC/SC)"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://pcsclite.apdu.fr"
source = f"https://pcsclite.apdu.fr/files/pcsc-lite-{pkgver}.tar.bz2"
sha256 = "5edcaf5d4544403bdab6ee2b5d6c02c6f97ea64eebf0825b8d0fa61ba417dada"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()

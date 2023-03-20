pkgname = "pcsclite"
pkgver = "1.9.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-libsystemd"]
hostmakedepends = ["pkgconf", "flex", "perl"]
makedepends = ["libusb-devel", "udev-devel", "polkit-devel"]
pkgdesc = "Middleware to access a smart card using SCard API (PC/SC)"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://pcsclite.apdu.fr"
source = f"https://pcsclite.apdu.fr/files/pcsc-lite-{pkgver}.tar.bz2"
sha256 = "502d80c557ecbee285eb99fe8703eeb667bcfe067577467b50efe3420d1b2289"


def post_install(self):
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsclite-devel")
def _devel(self):
    return self.default_devel()

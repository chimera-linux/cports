pkgname = "pcsc-lite"
pkgver = "1.9.9"
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
sha256 = "cbcc3b34c61f53291cecc0d831423c94d437b188eb2b97b7febc08de1c914e8a"


def post_install(self):
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

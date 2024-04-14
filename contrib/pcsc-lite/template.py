pkgname = "pcsc-lite"
pkgver = "2.1.0"
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
sha256 = "85cab61cc744c81e2bc432656863293b8428d0136f079e3b12a84b335b5b35aa"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()

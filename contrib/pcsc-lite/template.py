pkgname = "pcsc-lite"
pkgver = "2.0.0"
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
sha256 = "d6c3e2b64510e5ed6fcd3323febf2cc2a8e5fda5a6588c7671f2d77f9f189356"


def post_install(self):
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []

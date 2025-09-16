pkgname = "pcsc-lite"
pkgver = "2.3.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibsystemd=false",
    "-Dlibudev=true",
    "-Dpolkit=true",
    "-Dusb=true",
]
hostmakedepends = ["flex", "meson", "perl", "pkgconf"]
makedepends = ["dinit-chimera", "libusb-devel", "udev-devel", "polkit-devel"]
pkgdesc = "Middleware to access PC/SC smart cards using SCard API"
license = "BSD-3-Clause"
url = "https://pcsclite.apdu.fr"
source = f"https://pcsclite.apdu.fr/files/pcsc-lite-{pkgver}.tar.xz"
sha256 = "cdff7d7153a0b37aa74e26dfec89ec7dc5c5286aa21b91b903e38739d227e8e7"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "pcscd")


@subpackage("pcsc-lite-devel")
def _(self):
    return self.default_devel()

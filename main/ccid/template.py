pkgname = "ccid"
pkgver = "1.6.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dserial=true",
]
hostmakedepends = [
    "flex",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "libusb-devel",
    "pcsc-lite-devel",
    "udev-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "PC/SC driver to support CCID compliant readers"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-2.1-or-later"
url = "https://ccid.apdu.fr"
source = f"{url}/files/ccid-{pkgver}.tar.xz"
sha256 = "2eca8fb07e8fe7c0d39daeaca7b97cd73c40ed9b72738a24ad3dcbdfc918e1ea"


def post_install(self):
    self.install_file(
        "src/92_pcscd_ccid.rules", "usr/lib/udev/rules.d", mode=0o644
    )

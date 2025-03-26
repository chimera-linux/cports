pkgname = "ccid"
pkgver = "1.6.2"
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
license = "LGPL-2.1-or-later"
url = "https://ccid.apdu.fr"
source = f"{url}/files/ccid-{pkgver}.tar.xz"
sha256 = "41958410950157e622f9d91c9e78c7b708db74e22f71190c581d24d20564d449"


def post_install(self):
    self.install_file(
        "src/92_pcscd_ccid.rules", "usr/lib/udev/rules.d", mode=0o644
    )

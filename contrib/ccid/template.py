pkgname = "ccid"
pkgver = "1.6.0"
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
    "zlib-devel",
]
pkgdesc = "PC/SC driver to support CCID compliant readers"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-2.1-or-later"
url = "https://ccid.apdu.fr"
source = f"{url}/files/ccid-{pkgver}.tar.xz"
sha256 = "cdca7c22c45169cfc300d65d5362b7644ee195289f4fb8bf475a6cd321752c2c"


def post_install(self):
    self.install_file(
        "src/92_pcscd_ccid.rules", "usr/lib/udev/rules.d", mode=0o644
    )

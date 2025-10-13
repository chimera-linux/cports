pkgname = "ccid"
pkgver = "1.7.0"
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
sha256 = "2a040141109c1652caf06b41d9ed580b3ce706d478ebafd323b9085eb04e45a1"

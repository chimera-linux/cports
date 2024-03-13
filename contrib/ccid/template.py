pkgname = "ccid"
pkgver = "1.5.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-twinserial"]
configure_gen = []
hostmakedepends = ["automake", "libtool", "pkgconf", "flex", "perl"]
makedepends = ["zlib-devel", "pcsc-lite-devel", "udev-devel", "libusb-devel"]
pkgdesc = "PC/SC driver to support CCID compliant readers"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-2.1-or-later"
url = "https://ccid.apdu.fr"
source = f"{url}/files/ccid-{pkgver}.tar.bz2"
sha256 = "194708f75fe369d45dd7c15e8b3e8a7db8b49cfc5557574ca2a2e76ef12ca0ca"


def post_install(self):
    self.install_file(
        "src/92_pcscd_ccid.rules", "usr/lib/udev/rules.d", mode=0o644
    )

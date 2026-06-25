pkgname = "snapraid"
pkgver = "12.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-blkid",
]
hostmakedepends = [
    "autoconf",
    "automake",
]
makedepends = [
    "util-linux-blkid-devel",
]
pkgdesc = "Parity-based backup program for disk arrays"
license = "GPL-3.0-or-later"
url = "https://www.snapraid.it"
source = f"https://github.com/amadvance/snapraid/releases/download/v{pkgver}/snapraid-{pkgver}.tar.gz"
sha256 = "bc15ad9c42ddf9bd70033562a10e9b9fec43afed54c48fe22da4b6835657ec1b"


def post_install(self):
    self.install_license("COPYING")
    self.install_man("snapraid.1")

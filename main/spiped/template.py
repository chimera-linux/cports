pkgname = "spiped"
pkgver = "1.6.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["openssl3-devel"]
checkdepends = ["procps"]
pkgdesc = "Secure pipe daemon"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause"
url = "https://www.tarsnap.com/spiped.html"
source = f"https://www.tarsnap.com/spiped/spiped-{pkgver}.tgz"
sha256 = "70c53070dbbb10d1442754aeafb01b08ec829203d41023647dbf1a1435ee4a65"


def init_install(self):
    self.make_install_args = [
        f"BINDIR={self.chroot_destdir}/usr/bin",
        f"MAN1DIR={self.chroot_destdir}/usr/share/man/man1",
    ]


def post_install(self):
    self.install_license("COPYRIGHT")

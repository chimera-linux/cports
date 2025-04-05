pkgname = "spiped"
pkgver = "1.6.4"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["openssl3-devel"]
checkdepends = ["procps"]
pkgdesc = "Secure pipe daemon"
license = "BSD-2-Clause"
url = "https://www.tarsnap.com/spiped.html"
source = f"https://www.tarsnap.com/spiped/spiped-{pkgver}.tgz"
sha256 = "424fb4d3769d912b04de43d21cc32748cdfd3121c4f1d26d549992a54678e06a"


def init_install(self):
    self.make_install_args = [
        f"BINDIR={self.chroot_destdir}/usr/bin",
        f"MAN1DIR={self.chroot_destdir}/usr/share/man/man1",
    ]


def post_install(self):
    self.install_license("COPYRIGHT")

pkgname = "spiped"
pkgver = "1.6.2"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["openssl-devel"]
checkdepends = ["procps"]
pkgdesc = "Secure pipe daemon"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause"
url = "https://www.tarsnap.com/spiped.html"
source = f"https://www.tarsnap.com/spiped/spiped-{pkgver}.tgz"
sha256 = "05d4687d12d11d7f9888d43f3d80c541b7721c987038d085f71c91bb06204567"


def init_install(self):
    self.make_install_args = [
        f"BINDIR={self.chroot_destdir}/usr/bin",
        f"MAN1DIR={self.chroot_destdir}/usr/share/man/man1",
    ]


def post_install(self):
    self.install_license("COPYRIGHT")

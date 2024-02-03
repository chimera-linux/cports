pkgname = "txt2man"
pkgver = "1.7.1"
pkgrel = 0
hostmakedepends = ["gmake", "gawk"]
depends = ["gawk"]
pkgdesc = "Converts flat ASCII text to man page format"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/mvertes/txt2man"
source = f"{url}/archive/refs/tags/txt2man-{pkgver}.tar.gz"
sha256 = "4d9b1bfa2b7a5265b4e5cb3aebc1078323b029aa961b6836d8f96aba6a9e434d"


def do_install(self):
    self.do("gmake", "install", f"prefix={self.chroot_destdir}/usr")

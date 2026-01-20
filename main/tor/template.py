pkgname = "tor"
pkgver = "0.4.8.21"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-pic",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]

makedepends = [
    "libevent-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
    "xz-devel",
]

depends = [
    "libevent",
    "openssl3",
    "zlib-ng-compat",
]
options = ["!check"]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://www.torproject.org"
source = f"https://dist.torproject.org/tor-{pkgver}.tar.gz"
sha256 = "eaf6f5b73091b95576945eade98816ddff7cd005befe4d94718a6f766b840903"


def install(self):
    self.make.invoke(["install"], env={"DESTDIR": str(self.chroot_destdir)})
    self.install_license("LICENSE")

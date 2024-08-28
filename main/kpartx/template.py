pkgname = "kpartx"
pkgver = "0.9.9"
pkgrel = 0
build_wrksrc = "kpartx"
build_style = "makefile"
make_install_args = [
    "prefix=/usr",
    "libudevdir=/usr/lib/udev",
    "bindir=/usr/bin",
]
hostmakedepends = ["pkgconf"]
makedepends = ["device-mapper-devel"]
pkgdesc = "Create device maps from partition tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5c79219a7cce4eba5a196363ac121b9c0f3765e70e032889a5bf8e0c95de7bcb"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])

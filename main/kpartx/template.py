pkgname = "kpartx"
pkgver = "0.10.0"
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
sha256 = "f2e67a1d2167f3945afab6f0697207a03678f5b2bd80f1f45958c6fa1dfb8eef"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])

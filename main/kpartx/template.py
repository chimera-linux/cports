pkgname = "kpartx"
pkgver = "0.11.1"
pkgrel = 0
build_wrksrc = "kpartx"
build_style = "makefile"
make_install_args = [
    "prefix=/usr",
    "libudevdir=/usr/lib/udev",
    "bindir=/usr/bin",
]
hostmakedepends = ["pkgconf"]
makedepends = ["lvm2-devel"]
pkgdesc = "Create device maps from partition tables"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6cc57e33894ea2cd4c3bf1cbb9e4e8e7250d0699163b2907fcab1cd2e0123d85"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])

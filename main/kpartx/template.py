pkgname = "kpartx"
pkgver = "0.11.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0e7564e4984806006ec96134ea8823cfc461455675ce8aa5f363d94f696412f6"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])

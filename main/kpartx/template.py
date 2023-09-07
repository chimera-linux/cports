pkgname = "kpartx"
pkgver = "0.9.6"
pkgrel = 0
build_wrksrc = "kpartx"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "prefix=/usr",
    "libudevdir=/usr/lib/udev",
    "bindir=/usr/bin",
]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["device-mapper-devel"]
pkgdesc = "Create device maps from partition tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "401c6f6e8dc5d3feaaee76280716aee718579ac024ce4f2fae77c798dc7a0f9f"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def do_configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])

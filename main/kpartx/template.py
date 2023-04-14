pkgname = "kpartx"
pkgver = "0.9.5"
pkgrel = 0
build_wrksrc = "kpartx"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "prefix=/usr", "libudevdir=/usr/lib/udev", "bindir=/usr/bin"
]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["device-mapper-devel"]
pkgdesc = "Create device maps from partition tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e410fdee62ccaaecb79a0feb09c10d075a7254d013cf65543923bccb40c091c6"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]

def do_configure(self):
    self.make.invoke(None, ["-C", "..", "config.mk"])
